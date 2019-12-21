import vk_api
import csv
import datetime





                         

login = '+79251522134'
passwd = 'learnpythonparser'
vk_session = vk_api.VkApi(login, passwd)
vk_session.auth()
vk = vk_session.get_api()
group = str(-166725802) 


#получить количество постов  в группе
def get_count_posts_by_group_id (group_id): 
    wall_post = vk.wall.get(owner_id=group_id, count=1, offset= 0)
    total_posts_in_group = int (wall_post['count'])
    return total_posts_in_group

#получить ид конкретного поста
def get_post_id (group_id, posts_offset):

    wall_post = vk.wall.get(owner_id=group_id, count=1, offset= posts_offset) 
    #print(wall_post['items'][0]['id'])
    wall_post_id =  str( wall_post['items'][0]['id'])
   
    return wall_post_id

#получить сколько комментов у поста
def get_count_comments_by_post_id (group_id, post_id):
    comments_response = vk.wall.getComments(owner_id=group_id, post_id=post_id, count=1, sort='desc', offset=0) 
    comments_to_post = comments_response['count']
    #print('')
    #print (f'comments_to_post {comments_to_post}')
    return comments_to_post
   
#получить конкретный коммент   
def get_comment_by_post_and_offset (group_id, post_id, comment_offset):
    try:
        comments_response = vk.wall.getComments(owner_id=group_id, post_id=post_id, count=0, sort='desc', offset=comment_offset)
    
        comment = comments_response ['items'][0]['text']
        comment_id = comments_response ['items'][0]['id']
        comment_date = comments_response ['items'][0]['date']
    except: 
        comment_id = 'error'
        comment_date = 'error'
        comment = 'error'    
    
    return comment_id, comment_date, comment

#пишем в csv
def write_csv(data):
    with open('vk_news_new.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow(data)


total_posts_on_the_wall = get_count_posts_by_group_id (group)
print (f'total posts on the wall {total_posts_on_the_wall} wall id {group}')
print('')



for posts_number in range (5 ):#total_posts_on_the_wall ):

    current_post_to_parse_id =  get_post_id(group,posts_number)


    total_comments_to_parse_from_post = int (get_count_comments_by_post_id(group, current_post_to_parse_id))
    print (f'total comments to parse {total_comments_to_parse_from_post} from post {current_post_to_parse_id} posts offset {posts_number}')
    print ('')

    for comment_number in range (50): # (total_comments_to_parse_from_post):

        current_comment = get_comment_by_post_and_offset(group, current_post_to_parse_id, comment_number)
        write_csv (current_comment)
        print (f'comment number {str (comment_number)}')
        print (current_comment)

