from xml.etree.ElementTree import Element, SubElement, Comment, tostring


def add_action(x, y, action_type, mode):
    pass


def add_person(person_id, action_type, home_x, home_y, work_x, work_y, mode):
    global plans
    person = SubElement(plans, 'person')
    person.set('id', person_id)
    plan = SubElement(person, 'plan')
    action = SubElement(plan, 'act')
    action.set('type', action_type)
    action.set('x', home_x)
    action.set('y', home_y)
    action.set('end_time', '06:00:00')
    leg = SubElement(plan, 'leg')
    leg.set('mode', mode)


# create the file structure
plans = Element('plans')
plans.set('xml:lang', 'de-CH')
add_person(person_id='1', action_type='h', mode='car', home_x='1366533.3480765193', home_y='6678121.425384228')

# create a new XML file with the results
plans = tostring(plans, encoding='utf8', method='xml').decode()
plans_file = open("plans100.xml", "w")
plans_file.write(plans)
plans_file.close()
