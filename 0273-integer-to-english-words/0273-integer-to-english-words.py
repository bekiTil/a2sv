class Solution:
    def numberToWords(self, num: int) -> str:
        first = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven","Eight", "Nine"]
        second = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen","Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        third = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
               "Sixty", "Seventy", "Eighty", "Ninety"]

        def create(number):

            string = ""
            if number // 10**9:
                string += create(number // 10**9)+" Billion "+create(number % 10**9)
            elif number//10**6:
                string += create(number // 10**6)+" Million "+create(number % 10**6)
            elif number // 10**3:
                string += create(number // 10**3)+" Thousand "+create(number % 10**3)
            elif number // 100:
                string += create(number // 100)+" Hundred "+create(number % 100)
            elif number // 10:
                if number >= 10 and number <= 19:
                    string += second[number % 10]
                else:
                    string += third[number // 10] +" " + create(number % 10)
            else:
                string += first[number % 10]

            return string.strip()

        if not num:
            return "Zero"
        return (create(num)).strip()