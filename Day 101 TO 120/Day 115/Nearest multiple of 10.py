    # Nearest multiple of 10

    # A string s is given to represent a positive number. The task is to round str to the nearest multiple of 10.  If you have two multiples equally apart from s, choose the smallest element among them.

    # Examples:

    # Input: s = "29" 
    # Output: 30
    # Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29. 
    # Input: s = "15"
    # Output: 10
    # Explanation: 10 and 20 are equally distant multiples from 20. The smallest of the two is 10.
    


class Solution:

    def roundToNearest(self, num_str: str) -> str:
        n = len(num_str)

        if int(num_str[-1]) <= 5:
           
            num_str = num_str[:-1] + '0'
            return num_str

      
        else:
        
            num_str = num_str[:-1] + '0'
            carry = 1

            
            num_str_list = list(num_str)
            i = n - 2
            while i >= 0 and carry == 1:
                current_digit = int(num_str_list[i]) + carry

               
                if current_digit > 9:
                    carry = 1
                    current_digit = 0
                else:
                    carry = 0

         
                num_str_list[i] = str(current_digit)
                i -= 1

           
            if carry == 1:
                num_str_list.insert(0, '1')

            return ''.join(num_str_list)