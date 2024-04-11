@metadata_reactor
def set_router_id(metadata):
    main_interface_ip = metadata.get(f"interfaces/{ metadata.get('main_interface') }/ip_addresses")[0]

    return {
        'bird': {
            'router_id': metadata.get('bird/router_id', main_interface_ip)
        }
    }
