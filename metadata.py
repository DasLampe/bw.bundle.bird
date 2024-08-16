@metadata_reactor
def set_router_id(metadata):
    main_interface_ip = metadata.get(f"interfaces/{ metadata.get('main_interface') }/ip_addresses")[0]

    return {
        'bird': {
            'router_id': metadata.get('bird/router_id', main_interface_ip)
        }
    }
@metadata_reactor
def set_default_bgp_password(metadata):
    return_dict = {
        'bird': {
            'protocols': {
                'bgp': {},
            }
        }
    }

    local_as = metadata.get('bird/as')
    for name, cfg in metadata.get('bird/protocols/bgp', {}).items():
        return_dict['bird']['protocols']['bgp'][name] = {
            'password': repo.vault.password_for("bgp_password_{0}_to_{1}".format(*sorted([int(local_as), int(cfg.get('as'))])))
        }

    return return_dict

