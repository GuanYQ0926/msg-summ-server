import redis


# def read_redis(host, port, password):
def read_redis():
    try:
        # conn = redis.StrictRedis(host, port, password)
        # print(conn)
        # conn.ping
        # print('Connected to Remote Redis')
        # read
        message_list = [
            '''
            総務省統計委員会の点検検証部会は16日、毎月勤労統計（厚生労働省）
            の不正調査問題を受けた政府統計の追加点検結果を発表した。特に重要度の高い「基幹統計」（
            56統計）を除く「一般統計」（232統計）のうち154統計で不適切な対応があったと認定した。
            基幹統計の不適切対応（24統計）と合わせ、問題があったのは政府の288統計の6割強の178
            統計に上った。
            ''',
            '''
            最低賃金実態調査は最低賃金を算出するデータとして活用されているが、同部会は
            「重大な影響は生じない」としている。
            ''',
            '''
            同部会は同日、各府省に統計調査が適切に行われているか
            審査する課長級の専任担当者を配置するなどの再発防止策の素案も発表した。
            7月までに正式決定する方針。
            '''
        ]
        return message_list
    except Exception as e:
        print('Error: ', e)
        exit('Fail to Connect Remote Redis')
