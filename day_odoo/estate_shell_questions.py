# Beginner – Odoo Shell & Python Basics
# Print the number of properties with a garage
print(env['estate.property'].search_count([('garage', '=', True)]))

# List the names of properties that have no tag
for prop in env['estate.property'].search([('tag_ids', '=', False)]):
    print(prop.name)

# Set the 'garden_area' to 0 for all properties that have no garden
env['estate.property'].search([('garden', '=', False)]).write({'garden_area': 0})


# Intermediate – Business Logic & Automation
# Cancel properties with an expected price below 100,000 and no offers
for prop in env['estate.property'].search([('expected_price', '<', 100000)]):
    if not prop.offer_ids:
        prop.action_cancel()

# Auto-generate a unique reference for each property
for prop in env['estate.property'].search([]):
    prop.reference = f'PROP-{prop.id:05d}'

# For each partner, count how many offers they made and print it
Partner = env['res.partner']
Offer = env['estate.property.offer']
for partner in Partner.search([]):
    count = Offer.search_count([('partner_id', '=', partner.id)])
    if count:
        print(f'{partner.name}: {count} offer(s)')


# Advanced – Multi-Model Logic & Record Creation
# For each property in 'new' state for more than 60 days, set it to 'canceled'
from datetime import date, timedelta
threshold = date.today() - timedelta(days=60)
for prop in env['estate.property'].search([('state', '=', 'new')]):
    if prop.create_date.date() < threshold:
        prop.action_cancel()

# Create a property, assign it to the current user, and attach a dummy tag
user = env.user
tag = env['estate.property.tag'].search([], limit=1)
env['estate.property'].create({
    'name': 'Training Property',
    'expected_price': 150000,
    'salesperson_id': user.id,
    'tag_ids': [(4, tag.id)] if tag else [],
})

# Send a notification in the chatter of all properties with no offers
for prop in env['estate.property'].search([]):
    if not prop.offer_ids:
        prop.message_post(body='Reminder: No offers received.')

# Challenge – Real-World Scenarios
# Set the 'state' of all properties with an accepted offer and a selling_price > expected_price to 'sold'
for prop in env['estate.property'].search([('state', '=', 'offer_accepted')]):
    if prop.selling_price > prop.expected_price:
        prop.action_sold()

# Deactivate (archive) partners who have not made any offers
partners = env['res.partner'].search([])
offers = env['estate.property.offer'].read_group([('partner_id', '!=', False)], ['partner_id'], ['partner_id'])
partner_ids_with_offers = {r['partner_id'][0] for r in offers}
for partner in partners:
    if partner.id not in partner_ids_with_offers:
        partner.active = False

# Additional Challenges – Advanced Logic and Automation
# Create a summary dictionary of property count per state and print it
from collections import Counter
states = env['estate.property'].read_group([], ['state'], ['state'])
summary = {rec['state']: rec['state_count'] for rec in states}
print(summary)
# Create a custom notification on properties where the total area exceeds 300m2
for prop in env['estate.property'].search([]):
    if prop.total_area > 300:
        prop.message_post(body='Note: This is a large property.')
# Update all 'offer_accepted' properties to assign the buyer_id from the accepted offer
for prop in env['estate.property'].search([('state', '=', 'offer_accepted')]):
    accepted_offer = prop.offer_ids.filtered(lambda o: o.state == 'accepted')
    if accepted_offer:
        prop.buyer_id = accepted_offer.partner_id.id
# Create a new offer with a random price between 100k and 200k for each property missing one
import random
partner = env['res.partner'].search([], limit=1)
for prop in env['estate.property'].search([]):
    if not prop.offer_ids:
        env['estate.property.offer'].create({
            'property_id': prop.id,
            'partner_id': partner.id,
            'price': random.randint(100000, 200000),
        })
# Assign a default tag to any property missing tags and currently in 'new' state
tag = env['estate.property.tag'].search([('name', '=', 'Default')], limit=1)
if not tag:
    tag = env['estate.property.tag'].create({'name': 'Default'})
for prop in env['estate.property'].search([('state', '=', 'new'), ('tag_ids', '=', False)]):
    prop.write({'tag_ids': [(4, tag.id)]})
# Post a message on all properties where selling_price is set but no buyer is linked
for prop in env['estate.property'].search([('selling_price', '>', 0), ('buyer_id', '=', False)]):
    prop.message_post(body='Warning: Selling price is set, but no buyer assigned.')
# Archive all offers that are in 'refused' state and older than 60 days
from datetime import date, timedelta
threshold = date.today() - timedelta(days=60)
env['estate.property.offer'].search([
    ('state', '=', 'refused'),
    ('create_date', '<', threshold.isoformat()),
]).write({'active': False})
# Automatically mark properties as 'sold' if they have a selling price and a buyer assigned
for prop in env['estate.property'].search([('state', '!=', 'sold')]):
    if prop.buyer_id and prop.selling_price > 0:
        prop.action_sold()
# Add a log note to every property with more than 2 offers
for prop in env['estate.property'].search([]):
    if len(prop.offer_ids) > 2:
        prop.message_post(body='This property has more than two offers.')
# Cancel all offers with a price below 50% of the expected price of their property
for offer in env['estate.property.offer'].search([]):
    if offer.price < 0.5 * offer.property_id.expected_price:
        offer.action_refuse()
# Create a monthly digest: Count how many properties were sold this month
from datetime import date
today = date.today()
start_month = today.replace(day=1)
sold_this_month = env['estate.property'].search_count([
    ('state', '=', 'sold'),
    ('write_date', '>=', start_month.isoformat())
])
print(f'Properties sold this month: {sold_this_month}')
# Increase expected_price by 5% for all active properties in 'new' state
for prop in env['estate.property'].search([('state', '=', 'new'), ('active', '=', True)]):
    prop.expected_price *= 1.05

