from xml.etree.ElementTree import Element, SubElement, Comment, tostring


class PlansElementTree:
    pass


def add_action(parent, action, x_coordinate, y_coordinate, action_type, mode):
    return action


def add_person(person_id, action_type, home_x, home_y, work_x, work_y, mode):
    global plans
    person = SubElement(plans, 'person')
    person.set('id', person_id)
    plan = SubElement(person, 'plan')
    action = SubElement(plan, 'act')
    action.set('type', action_type)
    action.set('x', home_x)
    action.set('y', home_y)
    action.set('end_time', kwargs['leaving_home_time'])
    leg = SubElement(plan, 'leg')
    leg.set('mode', transportation_mode)


# create the file structure
plans = Element('plans')
plans.set('xml:lang', 'de-CH')

for x in range(10):
    add_person(person_id=str(x), action_type='h', transportation_mode='car', home_x='1366533.3480765193',
               home_y='6678121.425384228', leaving_home_time='08:00:00')

# create a new XML file with the results
plans = tostring(plans, encoding='utf8', method='xml').decode()
plans_file = open("plans100.xml", "w")
plans_file.write(plans)
plans_file.close()
