# Cool and interesting appraoches

## Pure Math approaches

**python**
```
class Solution:
    def shuffle(self, numbers, quantity):
        return [numbers[i//2 + i % 2 * quantity] for i in range(len(numbers))]

```
