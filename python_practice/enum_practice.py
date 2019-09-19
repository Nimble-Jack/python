from enum import Enum

permissions = ["can_manage_label", "can_manage_custom_intel", "can_manage_appliances", "can_access_kibana"]

class TriageWidgetXpaths(Enum):
    active_intrusion = '//card-header[contains(text(), "Active intrusions in my network")]'
    hosts_in_network = '//card-header[contains(text(),"Hosts in my network")]'
    my_work = '//card-header[contains(text(),"My work")]'
    quick_actions = '//card-header[contains(text(),"Quick actions")]'


def _are_triage_widgets_visible():
    """
    Check to see if all the widgets on the triage page loaded
    :return bool: True if visible, else False
    """
    visible_widgets = []

    for widget in TriageWidgetXpaths:
        #v = widget.value
        #n = widget.name
        #print("value %s" % v)
        #print("name %s" % n)
        visible_widgets.append(widget.name)
    print(visible_widgets)
_are_triage_widgets_visible()



#----
class TriageWidgetApiCalls(enum.Enum):
    active_intrusion = ''
    hosts_in_network = ''
    my_work = ''
    quick_actions = ''


def _does_widget_make_correct_api_call_and_have_data(self):
        """
        Verify that the widgets are making the correct API calls and that the calls return data
        :return bool: True if correct api and data, else False
        """
        """
        Sudo code:
        incorrect_api = []
        for widget in TriageWidgetXpaths:
            found_api_call = (get the api call from UI for each widget)
            if found_api_call != TriageWidgetApiCalls.(widget.name).value
                failed_api = '%s : %s' % (widget.name, found_api_call)
                incorrect_api.append(failed_api)
        if len(incorrect_api) != 0:
           self._logger.info('Incorrect APIs: %s' % incorrect_api)
           return False
        return True

        """
        pass
