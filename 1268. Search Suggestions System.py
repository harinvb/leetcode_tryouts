from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        results = []
        products.sort()
        for i in range(len(searchWord)):
            products = list(filter(lambda product: len(product) > i and product[i] == searchWord[i], products))
            results.append(products[:3])
        return results


print(Solution().suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
                                   searchWord="mouse"))
