from helper import rd_


def add_rank(book_id):
    isExist = False
    if rd_.exists('WeekRank'):
        isExist = True

    rd_.zincrby('WeekRank', book_id)

    if not isExist:  # 刚刚新增的Key
        rd_.expire('WeekRank', 7*24*3600)  # 设置Key的有效时长为1周


def get_week_rank_ids(top_n):
    week_rank_ids = rd_.zrevrange('WeekRank',0, top_n-1)
    return [int(id_.decode()) for id_ in week_rank_ids]