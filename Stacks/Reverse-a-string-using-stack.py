from stack_using_linkedlist import Stack
class solution:
      def reverseastring(self,data):
         s1=[]
         s=Stack()
         for i in data:
            s.push(i)
         while not s.isEmpty():
           s1.append(s.pop())
         s1="".join( s1 )
         return s1
data = input("Enter the string to be reversed: ")
s = solution()
print(s.reverseastring(data))

        


    

