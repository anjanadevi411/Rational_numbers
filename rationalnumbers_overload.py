
class RationalNumbers:
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom

    def compute_gcd(self, sample, sample1):
        if sample and sample1 != 0:
            if sample > sample1:
                num = sample1
            else:
                num = sample
            for i in range(1, num + 1):
                if ((sample % i == 0) and (sample1 % i == 0)):
                    computed_gcd = i
            # print(computed_gcd)
            return computed_gcd
        else:
            raise ValueError("cannot divide by zero")
            #return f"Give non-zero denominator values:"

    def compute_lcm(self, sample, sample1):
        if sample and sample1 != 0:
            lcm = (sample * sample1) // self.compute_gcd(sample, sample1)
            return lcm
        else:
            raise ValueError("cannot divide by zero")
            #print("Enter non zero values: ")

    def __add__(self, other):
        if self.denom and other.denom != 0:
            lcm = self.compute_lcm(self.denom, other.denom)
            lcm_deno = lcm
            if self.denom == lcm_deno:
                numer = self.numer
            else:
                n = int(lcm_deno / self.denom)
                numer = self.numer * n
            if other.denom == lcm_deno:
                numer1 = other.numer
            else:
                n1 = int(lcm_deno / other.denom)
                numer1 = other.numer * n1
            sum_numer = numer + numer1
            computed_gcd = self.compute_gcd(abs(sum_numer), abs(lcm_deno))
            sum_numer = sum_numer // computed_gcd
            lcm_deno = lcm_deno // computed_gcd
            return str(sum_numer)+"/" +str(lcm_deno)
        else:
            raise ValueError("cannot divide by zero")
            #print("Enter non zero denominator values")

    def __sub__(self, other):
        if self.denom and other.denom != 0:
            lcm = self.compute_lcm(self.denom,other.denom)
            lcm_deno = lcm
            if self.denom == lcm_deno:
                numer = self.numer
            else:
                n = int(lcm_deno/self.denom)
                numer = self.numer*n
            if other.denom == lcm_deno:
                numer1 = other.numer
            else:
                n1 = int(lcm_deno / other.denom)
                numer1 = other.numer * n1
            sub_numer = numer - numer1
            #print(sub_numer, "/" ,lcm_deno)
            if sub_numer != 0:
                computed_gcd = self.compute_gcd(abs(sub_numer), abs(lcm_deno))
                sub_numer = sub_numer // computed_gcd
                lcm_deno = lcm_deno // computed_gcd
                #print(int(sub_numer), "/", int(lcm_deno))
                return str(sub_numer)+"/" + str(lcm_deno)
            else:
                #print(int(sub_numer))
                return str(sub_numer)
        else:
            raise ValueError("cannot divide by zero")
            #print("Enter non-zero values: ")

    def __mul__(self, other):
        if self.denom and other.denom != 0:
            mul_numer = self.numer * other.numer
            mul_denom = self.denom * other.denom
            computed_gcd = self.compute_gcd(abs(mul_numer), abs(mul_denom))
            numer = mul_numer // computed_gcd
            deno = mul_denom // computed_gcd
            #print(int(numer), "/", int(deno))
            return str(numer) + "/" + str(deno)
        else:
            raise ValueError("cannot divide by zero")
            #print("Enter non zero values:")

    def __truediv__(self, other):
        if self.denom and other.denom != 0:
            div_numer = self.numer * other.denom
            div_denom = other.numer * self.denom
            computed_gcd = self.compute_gcd(abs(div_numer), abs(div_denom))
            numer = div_numer // computed_gcd
            deno = div_denom // computed_gcd
            if (numer/deno) > 0:
                return str(abs(numer))+"/"+str(abs(deno))
            else:
                return str(numer)+"/"+str(deno)
        else:
            raise ValueError("cannot divide by zero")
            #print("Enter non zero values: ")

if __name__ == '__main__':

    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")

    choose_operation = int(input('Enter the 1/2/3/4 respectivly : '))

    numerator = int(input('Enter the first numerator: '))
    denominator = int(input('Enter the first denominator: '))
    numerator1 = int(input('Enter the second numerator: '))
    denominator1 = int(input('Enter the second denominator: '))

    try:
        if denominator == 0 or denominator1 == 0:
            raise ValueError("denominators cannot be zero")
        R1 = RationalNumbers(numerator, denominator)
        R2 = RationalNumbers(numerator1,denominator1)

        if choose_operation == 1:
            addition = R1 + R2
            print(f'{numerator}/{denominator} + {numerator1}/{denominator1} = {addition}')
        elif choose_operation == 2:
            subtraction = R1 - R2
            print(f'{numerator}/{denominator} - {numerator1}/{denominator1} = {subtraction}')
        elif choose_operation == 3:
            multiplication = R1 * R2
            print(f'{numerator}/{denominator} * {numerator1}/{denominator1} = {multiplication}')
        elif choose_operation == 4:
            division = R1 / R2
            print(f'{numerator}/{denominator} / {numerator1}/{denominator1} = {division}')
        else:
            print('please enter appropriate option')
    except ValueError:
        print('Give non zero denominator values')