from parser_sdo import check_data,output,actions_on_site
from logic_table import launch_GUI
if __name__ == '__main__':
    actions_on_site()
    output()
    check_data(output())
    launch_GUI(check_data(output()))


