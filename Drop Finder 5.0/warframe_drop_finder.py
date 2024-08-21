import wf_db
import wf_debug
import wf_query
import wf_user_friendly

def main():
    
    if update:
        wf_db.create_new_db(URL)
    
    #wf_debug.print_items()
    
    #wf_debug.print_unique_mission_types()
    
    
    related_items = wf_debug.get_related_items(items)
    if show_related:
        print(related_items)
    
    report = wf_query.search_best_expected_return(related_items, time_scale=time_scale)
    
    wf_debug.display_report(report, report_length)
    pass

if __name__ == '__main__':
    
    URL = 'https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html'
    
    manual_input = False
    
    if manual_input:
        user_input = wf_user_friendly.user_input()
        
        update = user_input["update"]
        items = user_input["items"]
        show_related = user_input["show_related"]
        time_scale = user_input["time_scale"]
        report_length = user_input["report_length"]
    
    
    else:
    
        update = False
        items = ["Axi S17"]
        show_related = True
        time_scale = 20
        report_length = 5

    
    main()