def get_config(organization, common_args):    
    config = {
        'name': organization+'/caddy-docker-proxy-cache',
        'version': '2.7.5',
        'buildargs': {
            'CADDY_VERSION': '2.7.5',
        },
        'tests': ['--help'] # Just to test multi parameters commands
    }
    return config
