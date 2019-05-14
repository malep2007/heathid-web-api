
create_sales_prompts = '''
mutation{{
  createSalesprompts(
    productIds:[{product_id}],
    outletIds:[{outlet_id}],
    promptTitles:["{title}"],
    descriptions:["{description}"]
  ){{
  message
  }}
  }}

'''

incomplete_sales_entry = '''
mutation{{
  createSalesprompts(
    productIds:[{product_id},{product_id}],
    outletIds:[{outlet_id}],
    promptTitles:["{title}"],
    descriptions:["{description}"]
  ){{
  message
  }}
  }}

'''

update_sales_prompt = '''
mutation{{
   updateSalesprompt(id:{sales_prompt_id},
    promptTitle:"{title}",
    description:"{description}",
    productId:{product_id},
    outletId:{outlet_id}){{
    salesPrompt{{
      id
      promptTitle
      description
    }}
    success
  }}
}}

'''


def delete_sales_prompt(sales_prompt_id):
    return f'''mutation{{
                deleteSalesprompt(id: {sales_prompt_id}){{success}}
                    }}'''


query_all_sales_prompt = '''
        query{
         salesPrompts{
                id
                promptTitle
                description
                product{
                  id
                  productName
                }
               }
}
'''


def query_a_sales_prompt(sales_prompt_id):
    return (f'''query{{salesPrompt(id: {sales_prompt_id}){{id}}}}''')


def create_promotion(promotion):
    return (f'''
            mutation {{
                createPromotion(
                    title: "{promotion['title']}",
                    promotionTypeId: "{promotion['promotion_type_id']}",
                    description: "{promotion['description']}",
                    discount: {promotion['discount']},
                    outletId: {promotion['outlet_id']}
                    ) {{
                    success
                    promotion {{
                        id
                    }}
                }}
            }}
    ''')


def retrieve_promotions(outlet_id):
    return (f'''
            query {{
                outletPromotions(outletId: {outlet_id}){{
                    id
                }}
            }}
    ''')


def update_promotion(promotion_id, promotion):
    return (f'''
            mutation {{
                updatePromotion(
                    promotionId: "{promotion_id}"
                    title: "{promotion}"
                ){{
                    success
                    promotion {{
                        id
                    }}
                }}
            }}
    ''')


def delete_promotion(promotion_id):
    return (f'''
            mutation {{
                deletePromotion(
                    promotionId: "{promotion_id}"
                ){{
                    success
                }}
            }}
    ''')


def create_promotion_type(name):
    return (f'''
            mutation {{
                createPromotionType(
                    name: "{name}"
                    ) {{
                    success
                    promotionType {{
                        id
                    }}
                }}
            }}
    ''')


def retrieve_promotion_types():
    return (f'''
            query {{
                promotionTypes{{
                    id
                }}
            }}
    ''')