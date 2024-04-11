cfg = node.metadata.get("bird", {})

pkg_apt = {
    'bird': {},
}

svc_systemd = {
    'bird.service': {
        'running': True,
        'enabled': True,
        'needs': [
            'pkg_apt:bird',
            'file:/etc/bird/bird.conf',
        ],
    },
}

files = {
    '/etc/bird/bird.conf': {
        'source': 'etc/bird/bird.conf.j2',
        'content_type': 'jinja2',
        'context': {
            'router_id': cfg.get('router_id'),
            'localAS': cfg.get('as'),
            'protocols': cfg.get('protocols', {}),
        },
        'mode': '0640',
        'owner': 'bird',
        'group': 'bird',
        'needs': [
            'pkg_apt:bird',
        ],
        'triggers': [
            'svc_systemd:bird.service:reload',
        ],
    },
}
