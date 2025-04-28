class Solution:
    # def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    #     result = [] # trueかfalseを入れる配列
    #     max_int = 0
    #     # candiesにextraで加えた新しい配列を作る ①
    #     addcandies = []
    #     for i in range(len(candies)):
    #         addcandies.append(candies[i] + extraCandies)

    #     # 元のcandiesで、最大の数を求める ②
    #     max_int = max(candies)
    #     # ①と②を比較して、②未満だったら、falseをresultリストに格納する。それ以外は全てtrueを入れる。
    #     for j in range(len(addcandies)):
    #         if (addcandies[j] < max_int):
    #             result.append(False)
    #         else:
    #             result.append(True)
        
    #     return result

    # 修正したバージョン(もっと短く)
    # def KidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    #     result = []
    #     max_int = max(candies)

    #     for candy in candies:
    #         if candy + extraCandies >= max_int:
    #             result.append(True)
    #         else:
    #             result.append(False)
    #     return result

# リスト内包表記で作るなら
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_int = max(candies)
        return [candy + extraCandies >= max_int for candy in candies]