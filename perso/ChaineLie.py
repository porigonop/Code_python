#!/usr/bin/env python3
class Item():

    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def __repr__(self):
        answer = "[" + str(self.item) + ", "
        current = self.next
        while True:
            answer += str(current.item) + ", "
            current = current.next
            if current == None:
                break
              
        return answer[:-2] + "]"
    
class Liste():
    
    def __init__(self, *element):
        A = Item(element[-1])
        for elt in range(len(element[:-1])):
        
            A = Item(element[-elt - 2], A)
                
        self.initial = A
        #à supprimer
        rev = Item(element[0])
        for elt in element[1:]:
            rev = Item(elt, rev)
            
        self.rev = rev
        
    def append(self, element):
        current = self.initial
        while True:
            
            if current.next == None:
                current.next = Item(element, None)
                break
            current = current.next
            
        self.rev = Item(element, self.rev)
        
    def pop(self, position):
        
        poping = self[postion]
        
        
        
        
        return poping
    
    def remove(self, position):
        
        pass
        
        
        
    def __getitem__(self, position):
        if len(liste) < position:
            raise IndexError("Sequence out of range")
        if position < 0:
            position = -position -1
            current = self.rev
        else:
            current = self.initial
        for i in range(position):
            current = current.next
        return current.item

    def __setitem__(self, position, value):
    
        if len(liste) < position:
            raise IndexError("Sequence out of range")
            
        if position < 0:
        
            position = - position
            
            current = self.rev
            for i in range(position - 1):
                current = current.next
            current.item = value
            
            other_current = self.initial
            lenght = len(self)
            for i in range(lenght - position):
                other_current = other_current.next
            
            other_current.item = value
            
            
        else:
        
            current = self.initial
            for i in range(position - 1):
                current = current.next
            current.item = value
            
            
            other_current = self.rev
            lenght = len(self)
            for i in range(lenght - position):
                other_current = other_current.next
            other_current.item = value
            

            
    def __len__(self):
    
        count = 0
        current = self.initial
        
        while True:
            if current == None:
                return count
            count += 1
            current = current.next
    
    def reverse(self):
        #à changer
        return self.rev
        
    def __repr__(self):
        return str(self.initial)
        
if __name__ == "__main__":
    liste = Liste(1,3,2)
    print(liste)
    print(liste.reverse())
    
    print(len(liste))
    liste.append(-1)
    liste.append("salut")
    
    print(len(liste))
    print(liste)
    print(liste.reverse())

    liste[3] = 0
    print(liste)
    print(liste.reverse())

    