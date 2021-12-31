import helper

organization = 'secsi'

api_results = {
    'LAST_UBUNTU_VERSION': helper.get_latest_docker_hub_version('ubuntu'),
    'BFAC_GITHUB_INFO':helper.get_latest_github_release_no_browser_download('mazen160/bfac'),
    'DIRHUNT_PIP_VERSION': helper.get_latest_pip_version('dirhunt'),
    'FFUF_GITHUB_INFO':  helper.get_latest_github_release('ffuf/ffuf', target_string='linux_amd64'),
    'FINDSPLOIT_GITHUB_INFO':  helper.get_latest_github_release_no_browser_download('1N3/Findsploit'),
    'GOBUSTER_GITHUB_INFO':  helper.get_latest_github_release('OJ/gobuster', target_string='linux-amd64'),
    'HYDRA_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('vanhauser-thc/thc-hydra'),
    'KNOCKPY_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('guelfoweb/knock'),
    'RETIRE_NPM_VERSION': helper.get_latest_npm_registry_version('retire'),
    'MASSCAN_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('robertdavidgraham/masscan'),
    'SUBLIST3R_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('aboul3la/Sublist3r'),
    'WHATWEB_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('urbanadventurer/WhatWeb'),
}

tools = {
    'bfac': {
        'name': organization+'/bfac',
        'version': api_results['BFAC_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'BFAC_DOWNLOAD_URL': api_results['BFAC_GITHUB_INFO']['url']
        }
    },
    'dirb': {
        'name': organization+'/dirb',
        'version': '2.22',
        'buildargs': {
            'LAST_UBUNTU_VERSION': api_results['LAST_UBUNTU_VERSION']
        }
    },
    'dirhunt': {
        'name': organization+'/dirhunt',
        'version': api_results['DIRHUNT_PIP_VERSION'],
        'buildargs': {
            'DIRHUNT_VERSION': api_results['DIRHUNT_PIP_VERSION']
        }
    },
    'ffuf': {
        'name': organization+'/ffuf',
        'version': api_results['FFUF_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LAST_UBUNTU_VERSION': api_results['LAST_UBUNTU_VERSION'],
            'FFUF_DOWNLOAD_URL': api_results['FFUF_GITHUB_INFO']['url']
        }
    },
    'findsploit': {
        'name': organization+'/findsploit',
        'version': api_results['FINDSPLOIT_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LAST_UBUNTU_VERSION': api_results['LAST_UBUNTU_VERSION'],
            'FINDSPLOIT_DOWNLOAD_URL': api_results['FINDSPLOIT_GITHUB_INFO']['url']
        }
    },
    'gobuster': {
        'name': organization+'/gobuster',
        'version': api_results['GOBUSTER_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LAST_UBUNTU_VERSION': api_results['LAST_UBUNTU_VERSION'],
            'GOBUSTER_DOWNLOAD_URL': api_results['GOBUSTER_GITHUB_INFO']['url']
        }
    },
    'hydra': {
        'name': organization+'/hydra',
        'version': api_results['HYDRA_GITHUB_INFO']['version'][1:], # Remove the leading 'v',
        'buildargs': {
            'LAST_UBUNTU_VERSION': api_results['LAST_UBUNTU_VERSION'],
            'HYDRA_DOWNLOAD_URL': api_results['HYDRA_GITHUB_INFO']['url']
        }
    },
    'knockpy': {
        'name': organization+'/knockpy',
        'version': api_results['KNOCKPY_GITHUB_INFO']['version'],
        'buildargs': {
            'KNOCKPY_DOWNLOAD_URL': api_results['KNOCKPY_GITHUB_INFO']['url']
        }
    },
    'retire': {
        'name': organization+'/retire',
        'version': api_results['RETIRE_NPM_VERSION'],
        'buildargs': {
            'RETIRE_NPM_VERSION': api_results['RETIRE_NPM_VERSION']
        }
    },
    'masscan': {
        'name': organization+'/masscan',
        'version': api_results['MASSCAN_GITHUB_INFO']['version'],
        'buildargs': {
            'LAST_UBUNTU_VERSION': api_results['LAST_UBUNTU_VERSION'],
            'MASSCAN_DOWNLOAD_URL': api_results['MASSCAN_GITHUB_INFO']['url']
        }
    },
    'sublist3r': {
        'name': organization+'/sublist3r',
        'version': api_results['SUBLIST3R_GITHUB_INFO']['version'],
        'buildargs': {
            'SUBLIST3R_DOWNLOAD_URL': api_results['SUBLIST3R_GITHUB_INFO']['url']
        }
    },
    'whatweb': {
        'name': organization+'/whatweb',
        'version': api_results['WHATWEB_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LAST_UBUNTU_VERSION': api_results['LAST_UBUNTU_VERSION'],
            'WHATWEB_DOWNLOAD_URL': api_results['WHATWEB_GITHUB_INFO']['url']
        }
    }
}

# List of all imported tools 
def get_tools():
    return tools

# Get a single tool for specific build
def get_single_tool(tool_name):
    tool = next((tools[t] for t in tools if t == tool_name), None) # returns None if tool is not found
    return tool 