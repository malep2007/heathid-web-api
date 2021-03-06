import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from healthid.apps.orders.models.orders import (
    SupplierOrderDetails, Order, OrderDetails)
from healthid.utils.app_utils.database import get_model_object
from healthid.apps.orders.models.suppliers import Suppliers
from healthid.utils.app_utils.pagination import pagination_query
from healthid.utils.app_utils.pagination_defaults import PAGINATION_DEFAULT
from healthid.utils.orders_utils.inventory_notification import \
    autosuggest_product_order
from healthid.utils.app_utils.check_user_in_outlet import \
    check_user_has_an_active_outlet


class AutosuggestOrder(graphene.ObjectType):
    product_name = graphene.String()
    suggested_quantity = graphene.String()


class OrderType(DjangoObjectType):
    class Meta:
        model = Order


class OrderDetailsType(DjangoObjectType):
    class Meta:
        model = OrderDetails


class SupplierOrderDetailsType(DjangoObjectType):
    order_details = graphene.List(OrderDetailsType)
    supplier_order_name = graphene.String()
    supplier_order_number = graphene.String()
    deliver_to = graphene.String()
    delivery_due = graphene.Date()
    payment_due = graphene.Date()

    class Meta:
        model = SupplierOrderDetails

    def resolve_order_details(self, info, **kwargs):
        """
        get order details

        Returns:
            list: order details of a particular supplier and order
        """
        return self.get_order_details

    def resolve_supplier_order_name(self, info, **kwargs):
        """
        gets supplier order name

        Returns:
            string: supplier order name from supplier order details
        """
        return self.get_supplier_order_name

    def resolve_supplier_order_number(self, info, **kwargs):
        """
        gets supplier order number

        Returns:
            string: supplier order number from supplier order details
        """
        return self.get_supplier_order_number

    def resolve_deliver_to(self, info, **kwargs):
        """
        gets outlets a supplier is supposed to deliver the order to

        Returns:
            list: outlets supplier is supposed to deliver to from
                  supplier order details
        """
        return self.deliver_to_outlets

    def resolve_delivery_due(self, info, **kwargs):
        """
        gets the date a supplier is supposed to deliver the order

        Returns:
            date: date when the supplier has to deliver order from
                  supplier order details
        """
        return self.delivery_due_date

    def resolve_payment_due(self, info, **kwargs):
        """
        gets when the payment of the supplier should be paid

        Returns:
            date: when the supplier will be paid from the supplier
                  order details
        """
        return self.payment_due_date


class Query(graphene.AbstractType):

    suppliers_order_details = graphene.List(
        SupplierOrderDetailsType, order_id=graphene.Int(required=True))
    supplier_order_details = graphene.Field(
        SupplierOrderDetailsType, order_id=graphene.Int(required=True),
        supplier_id=graphene.String(required=True)
    )
    orders = graphene.List(OrderType, page_count=graphene.Int(),
                           page_number=graphene.Int())
    order = graphene.Field(OrderType, order_id=graphene.Int(required=True))
    open_orders = graphene.List(OrderType, page_count=graphene.Int(),
                                page_number=graphene.Int())
    closed_orders = graphene.List(OrderType, page_count=graphene.Int(),
                                  page_number=graphene.Int())
    total_orders_pages_count = graphene.Int()
    pagination_result = None
    autosuggest_product_order = graphene.List(AutosuggestOrder)

    @login_required
    def resolve_suppliers_order_details(self, info, **kwargs):
        """
        gets order details for suppliers of that order

        Returns:
            list: supplier order details of a particular order
        """
        order = get_model_object(Order, 'id', kwargs.get('order_id'))
        return SupplierOrderDetails.objects.filter(order=order)

    @login_required
    def resolve_supplier_order_details(self, info, **kwargs):
        order = get_model_object(Order, 'id', kwargs.get('order_id'))
        supplier = get_model_object(Suppliers, 'id', kwargs.get('supplier_id'))
        return SupplierOrderDetails.objects.filter(order=order,
                                                   supplier=supplier).first()

    @login_required
    def resolve_orders(self, info, **kwargs):
        """
        gets all orders

        Returns:
            list: orders
        """
        page_count = kwargs.get('page_count')
        page_number = kwargs.get('page_number')
        orders_set = Order.objects.all().order_by('id')
        if page_count or page_number:
            orders = pagination_query(
                orders_set, page_count, page_number)
            Query.pagination_result = orders
            return orders[0]
        paginated_response = pagination_query(orders_set,
                                              PAGINATION_DEFAULT[
                                                  "page_count"],
                                              PAGINATION_DEFAULT[
                                                  "page_number"])
        Query.pagination_result = paginated_response
        return paginated_response[0]

    @login_required
    def resolve_total_orders_pages_count(self, info, **kwargs):
        """
        :param info:
        :param kwargs:
        :return: Total number of pages for a specific pagination response
        :Note: During querying, totalOrdersPagesCount query field should
        strictly be called after the orders query when the pagination
        is being applied, this is due to GraphQL order of resolver methods
        execution.
        """
        if not Query.pagination_result:
            return 0
        return Query.pagination_result[1]

    @login_required
    def resolve_order(self, info, **kwargs):
        """
        gets a single order

        Returns:
            obj: an order
        """
        return get_model_object(Order, 'id', kwargs.get('order_id'))

    @login_required
    def resolve_open_orders(self, info, **kwargs):
        """
        gets orders that are open

        Returns:
            list: open orders
        """
        page_count = kwargs.get('page_count')
        page_number = kwargs.get('page_number')
        open_orders_set = Order.objects.filter(closed=False).order_by('id')
        if page_count or page_number:
            open_orders = pagination_query(
                open_orders_set, page_count, page_number)
            Query.pagination_result = open_orders
            return open_orders[0]
        paginated_response = pagination_query(open_orders_set,
                                              PAGINATION_DEFAULT[
                                                  "page_count"],
                                              PAGINATION_DEFAULT[
                                                  "page_number"])
        Query.pagination_result = paginated_response
        return paginated_response[0]

    @login_required
    def resolve_closed_orders(self, info, **kwargs):
        """
        gets orders that have been closed

        Returns:
            list: closed orders
        """
        page_count = kwargs.get('page_count')
        page_number = kwargs.get('page_number')
        closed_orders_set = Order.objects.filter(closed=True).order_by('id')
        if page_count or page_number:
            closed_orders = pagination_query(
                closed_orders_set, page_count, page_number)
            Query.pagination_result = closed_orders
            return closed_orders[0]
        paginated_response = pagination_query(closed_orders_set,
                                              PAGINATION_DEFAULT[
                                                  "page_count"],
                                              PAGINATION_DEFAULT[
                                                  "page_number"])
        Query.pagination_result = paginated_response
        return paginated_response[0]

    @login_required
    def resolve_autosuggest_product_order(self, info, **kwargs):
        """
        Auto suggest products that needs to be ordered and the
        quantity that needs to be ordered for based on the sales
        velocity calculator

        Returns:
            list: tuple(product_name, quantity)
        """
        user = info.context.user
        outlet = check_user_has_an_active_outlet(user)
        product_to_order = autosuggest_product_order(outlet=outlet)
        return product_to_order
