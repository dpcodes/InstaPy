# additional imports random amount for interactions
import random
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = 'nativobike.poa'
insta_password = 'di3g0C4ld3ir4'

#GENERAL SETTINGS
# restrictions
dont_likes = ['#exactmatch', '[startswith', ']endswith', 'broadmatch']
ignore_users = []

# prevent commenting on and unfollowing your good friends (the images will still be liked)
friends = []

# prevent posts that contain
ignore_list = []

# TARGET SETTINGS
# set similar accounts and influencers from your niche to target
targets = ['atritobmx', 'world_mtb_', 'maisbikebrasil', 'caloi', 'monark', 'bike']
# skip all business accounts, except from list given
target_business_categories = ['ciclismo', 'bicicleta', 'bike']

# COMMENT SETTINGS
comments = ['Que Legaal ;)', 'Que Bacanaa :)', 'Que Massa =)', 'Continue postando, adoro suas postagens :)']

#LOGIN-DATA
session = InstaPy(username=insta_username,
                      password=insta_password,
                      	headless_browser=True,
                      		disable_image_load=True,
                      			multi_logs=True)

with smart_run(session):

    # HEY HO LETS GO
    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)
    session.set_ignore_users(ignore_users)
    session.set_simulation(enabled=True)
    session.set_relationship_bounds(enabled=True,
                 potency_ratio=None,
                  delimit_by_numbers=True,
                   max_followers=7500,
                    max_following=3000,
                     min_followers=25,
                      min_following=25,
                       min_posts=10)
    session.set_skip_users(skip_private=True,
                                skip_no_profile_pic=True,
                                skip_business=True,
                                dont_skip_business_categories=[target_business_categories])

    session.set_user_interact(amount=3, randomize=True, percentage=80, media='Photo')
    session.set_do_like(enabled=True, percentage=90)
    session.set_do_comment(enabled=True, percentage=15)
    session.set_comments([comments], media='Photo')
    session.set_do_follow(enabled=True, percentage=40, times=1)

    # TARGETING   
    # select users form a list of a predefined targets
    number = random.randint(3, 5)
    random_targets = targets
    if len(targets) <= number:
        random_targets = targets
    else:
        random_targets = random.sample(targets, number)

    # interact with the chosen targets
    session.follow_user_followers(random_targets, amount=random.randint(30,60), randomize=True, sleep_delay=600, interact=True)

    # UNFOLLOW
    # unfollow nonfollowers after one day
    session.unfollow_users(amount=random.randint(75,100), InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=24*60*60, sleep_delay=600)
    # unfollow all users followed by instapy after one week to keep the following-level clean
    session.unfollow_users(amount=random.randint(75,100), InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=168*60*60, sleep_delay=600)