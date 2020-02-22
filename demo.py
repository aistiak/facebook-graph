
import facebook 

act = "pest_your access token hear"
def get_fb_group_posts():

    graph = facebook.GraphAPI(access_token=act)
    response = graph.get_object(id='325584160964557',fields='feed.limit(1)')
    # posts = response.data
    posts = response['feed']['data']

    print(posts)

    return response

get_fb_group_posts()