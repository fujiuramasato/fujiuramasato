file_path = './result_tweet.txt'
def tweet_counter_by_cluster(file_path):
    counter = 0
    fp = open(file_path)
    cluster_number = 1
    cluster_dict = {}
    for line in fp.readlines(): 
        line = line.replace('\n', '')
        line_list = line.split('\t') 
        if ')-------------------------クラスタ' in line:
            cluster_number +=1
        else:
            if line != '':
                if cluster_number in cluster_dict:
                    cluster_dict[cluster_number].append(line)
                else:
                    cluster_dict.append(cluster_number, line_list)
    for cluster in cluster_dict:
        counter += len(cluster)
    return counter   

print(tweet_counter_by_cluster(file_path))