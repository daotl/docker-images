import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_tag_no_browser_download('d3mondev/puredns'),
    }
    
    config = {
        'name': organization+'/puredns',
        'version': api_results['GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'DOWNLOAD_URL': api_results['GITHUB_INFO']['url'],
            'GOLANG_ALPINE_VERSION' : common_args['GOLANG_ALPINE_VERSION']
        },
        'tests': ['-h']
    }
    return config