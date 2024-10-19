import math


class Vector2:
    def __init__(self,x:float,y:float):
        if type(x) == float or type(x) == int and type(y) == float or type(y) == int:
            self.x = x
            self.y = y
        else: 
            raise ValueError("X and Y must be type float or int!")     
    def len(self):
        return math.hypot(self.x,self.y)
    def __abs__(self):
        return Vector2(abs(self.x),abs(self.y))  
    def __round__(self,stage):
        return Vector2(round(self.x,stage),round(self.y,stage))
    def __floor__(self):
        return Vector2(math.floor(self.x),math.floor(self.y))  
    def __trunc__(self):
        return Vector2(math.trunc(self.x),math.trunc(self.y))    
    def __ceil__(self):
        return Vector2(math.ceil(self.x),math.ceil(self.y))  
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    def __delattr__(self,*args):
        raise TypeError("Delete not allowed!")    
    def __lshift__(self,value):
        a = ToVector2(value)
        return Vector2(self.x<<a.x,self.y<<a.y)                      
    def __rshift__(self,value):
        a = ToVector2(value)
        return Vector2(self.x>>a.x,self.y>>a.y)             
    def __invert__(self):
        return Vector2(~self.x,~self.y)      
    def __or__(self, value):
        a = ToVector2(value)
        return Vector2(self.x|a.x,self.y|a.y)            
    def __xor__(self, value):
        a = ToVector2(value)
        return Vector2(self.x^a.x,self.y^a.y)           
    def __and__(self, value):
        a = ToVector2(value)
        return Vector2(self.x&a.x,self.y&a.y)         
    def __rlshift__(self,value):
        a = ToVector2(value)
        self = Vector2(self.x<<a.x,self.y<<a.y)                      
    def __rrshift__(self,value):
        a = ToVector2(value)
        self = Vector2(self.x>>a.x,self.y>>a.y)                
    def __ror__(self, value):
        a = ToVector2(value)
        self = Vector2(self.x|a.x,self.y|a.y)            
    def __rxor__(self, value):
        a = ToVector2(value)
        self = Vector2(self.x^a.x,self.y^a.y)           
    def __rand__(self, value):
        a = ToVector2(value)
        self = Vector2(self.x&a.x,self.y&a.y)   
    def __add__(self,arg):
        a = ToVector2(arg)
        return Vector2(self.x+a.x,self.y+a.y)
    def __sub__(self,arg):
        a = ToVector2(arg)
        return Vector2(self.x-a.x,self.y-a.y)
    def __mul__(self,arg):
        a = ToVector2(arg)
        return Vector2(self.x*a.x,self.y*a.y)
    def __div__(self,arg):
        a = ToVector2(arg)
        return Vector2(self.x/a.x,self.y/a.y)
    def __truediv__(self,arg):
        return self.__div__(arg)
    def __floordiv__(self,arg):
        return math.floor(self.__div__(arg))   
    def __mod__(self,arg):
        a = ToVector2(arg)        
        return Vector2(self.x%a.x,self.y%a.y)
    def sqrt(self):
         return Vector2(math.sqrt(self.x),math.sqrt(self.y))    
    def __pow__(self,value):
        a = ToVector2(value)        
        return Vector2(self.x**a.x,self.y**a.y)      
    def __eq__(self,arg):
        a = ToVector2(arg)        
        return self.x == a.x and self.y == a.y
    def __le__(self,arg):
        a = ToVector2(arg)        
        return self.x <= a.x and self.y <= a.y            
    def __lt__(self,arg):
        a = ToVector2(arg)        
        return self.x < a.x and self.y < a.y
    def __ne__(self,arg):
        a = ToVector2(arg)        
        return self.x != a.x and self.y != a.y
    def __gt__(self,arg):
        a = ToVector2(arg)        
        return self.x > a.x and self.y > a.y           
    def __ge__(self,arg):
        a = ToVector2(arg)        
        return self.x >= a.x and self.y >= a.y
    def __iter__(self):
        return iter([self.x,self.y])
    def __list__(self):
        return [self.x,self.y]
    def __dict__(self):
        return {"x":self.x,"y":self.y}
    def __bool__(self):
        if self.x != 0 and self.y != 0:
            return True
        return False
    def __tuple__(self):
        return (self.x,self.y)
    def __float__(self):
        return float(self.x + self.y)
    def __int__(self):
        return int(self.x + self.y)    
    def __str__(self):
        return  f"x:{str(self.x)} y: {str(self.y)}"      
    def __radd__(self,arg):
        a = ToVector2(arg)
        self = Vector2(self.x+a.x,self.y+a.y)
    def __rsub__(self,arg):
        a = ToVector2(arg)
        self =  Vector2(self.x-a.x,self.y-a.y)
    def __rmul__(self,arg):
        a = ToVector2(arg)
        self = Vector2(self.x*a.x,self.y*a.y)
    def __rdiv__(self,arg):
        a = ToVector2(arg)
        self = Vector2(self.x/a.x,self.y/a.y) 
    def __rmod__(self,arg):
        a = ToVector2(arg)        
        self = Vector2(self.x%a.x,self.y%a.y)
    def rsqrt(self):
        self = Vector2(math.sqrt(self.x),math.sqrt(self.y))    
    def __rpow__(self,value):
        a = ToVector2(value)        
        self = Vector2(self.x**a.x,self.y**a.y) 
    def oreq(self,arg):
        a = ToVector2(arg)        
        return self.x == a.x or self.y == a.y
    def orle(self,arg):
        a = ToVector2(arg)        
        return self.x <= a.x or self.y <= a.y              
    def orlt(self,arg):
        a = ToVector2(arg)        
        return self.x < a.x or self.y < a.y 
    def orne(self,arg):
        a = ToVector2(arg)        
        return self.x != a.x or self.y != a.y
    def orgt(self,arg):
        a = ToVector2(arg)        
        return self.x > a.x or self.y > a.y             
    def orge(self,arg):
        a = ToVector2(arg)        
        return self.x >= a.x or self.y >= a.y 
    def steq(self,arg):
        if type(arg) != Vector2:
            raise TypeError("Argument must be type Vector2")     
        return self == arg
    def stle(self,arg):
        if type(arg) != Vector2:
            raise TypeError("Argument must be type Vector2")     
        return self <= arg             
    def stlt(self,arg):
        if type(arg) != Vector2:
            raise TypeError("Argument must be type Vector2")     
        return self < arg  
    def stne(self,arg):
        if type(arg) != Vector2:
            raise TypeError("Argument must be type Vector2")     
        return self != arg
    def stgt(self,arg):
        if type(arg) != Vector2:
            raise TypeError("Argument must be type Vector2")     
        return self > arg           
    def stge(self,arg):
        if type(arg) != Vector2:
            raise TypeError("Argument must be type Vector2")     
        return self >= arg        

        



class Vector3:
    def __init__(self,x:float,y:float,z:float):
        if type(x) == float or type(x) == int and type(y) == float or type(y) == int and type(z) == float or type(z) == int:
            self.x = x
            self.y = y
            self.z = z   
        else:
            raise ValueError("X,Y and Z must be type float or int!")      
    def __abs__(self):
        return Vector3(abs(self.x),abs(self.y),abs(self.z))  
    def __round__(self,stage):
        return Vector3(round(self.x,stage),round(self.y,stage),round(self.z,stage))
    def __floor__(self):
        return Vector3(math.floor(self.x),math.floor(self.y),math.floor(self.z))  
    def __trunc__(self):
        return Vector3(math.trunc(self.x),math.trunc(self.y),math.trunc(self.z))    
    def __ceil__(self):
        return Vector3(math.ceil(self.x),math.ceil(self.y),math.ceil(self.z))  
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    def __delattr__(self,*args):
        raise TypeError("Delete not allowed!")
    def __lshift__(self,value):
        a = ToVector3(value)
        return Vector3(self.x<<a.x,self.y<<a.y,self.z<<a.z)                      
    def __rshift__(self,value):
        a = ToVector3(value)
        return Vector3(self.x>>a.x,self.y>>a.y,self.z>>a.z)             
    def __invert__(self):
        return Vector3(~self.x,~self.y,~self.z)      
    def __or__(self, value):
        a = ToVector3(value)
        return Vector3(self.x|a.x,self.y|a.y,self.z|a.z)            
    def __xor__(self, value):
        a = ToVector3(value)
        return Vector3(self.x^a.x,self.y^a.y,self.z^a.z)           
    def __and__(self, value):
        a = ToVector3(value)
        return Vector3(self.x&a.x,self.y&a.y,self.z&a.z)         
    def __rlshift__(self,value):
        a = ToVector3(value)
        self = Vector3(self.x<<a.x,self.y<<a.y,self.z<<a.z)                      
    def __rrshift__(self,value):
        a = ToVector3(value)
        self = Vector3(self.x>>a.x,self.y>>a.y,self.z>>a.z)                
    def __ror__(self, value):
        a = ToVector3(value)
        self = Vector3(self.x|a.x,self.y|a.y,self.z|a.z)            
    def __rxor__(self, value):
        a = ToVector3(value)
        self = Vector3(self.x^a.x,self.y^a.y,self.z^a.z)           
    def __rand__(self, value):
        a = ToVector3(value)
        self = Vector3(self.x&a.x,self.y&a.y,self.z&a.z)        
    def __add__(self,arg):
        a = ToVector3(arg)
        return Vector3(self.x+a.x,self.y+a.y,self.z+a.z)
    def __sub__(self,arg):
        a = ToVector3(arg)
        return Vector3(self.x-a.x,self.y-a.y,self.z-a.z)
    def __mul__(self,arg):
        a = ToVector3(arg)
        return Vector3(self.x*a.x,self.y*a.y,self.z*a.z)
    def __div__(self,arg):
        a = ToVector3(arg)
        return Vector3(self.x/a.x,self.y/a.y,self.z/a.z)
    def __truediv__(self,arg):
        return self.__div__(arg)
    def __floordiv__(self,arg):
        return math.floor(self.__div__(arg))   
    def __mod__(self,arg):
        a = ToVector3(arg)        
        return Vector3(self.x%a.x,self.y%a.y,self.z%a.z)
    def sqrt(self):
         return Vector3(math.sqrt(self.x),math.sqrt(self.y),math.sqrt(self.z))    
    def __pow__(self,value):
        a = ToVector3(value)        
        return Vector3(self.x**a.x,self.y**a.y,self.z**a.z)      
    def __radd__(self,arg):
        a = ToVector3(arg)
        self = Vector3(self.x+a.x,self.y+a.y,self.z+a.z)
    def __rsub__(self,arg):
        a = ToVector3(arg)
        self =  Vector3(self.x-a.x,self.y-a.y,self.z-a.z)
    def __rmul__(self,arg):
        a = ToVector3(arg)
        self = Vector3(self.x*a.x,self.y*a.y,self.z*a.z)
    def __rdiv__(self,arg):
        a = ToVector3(arg)
        self = Vector3(self.x/a.x,self.y/a.y,self.z/a.z) 
    def __rmod__(self,arg):
        a = ToVector3(arg)        
        self = Vector3(self.x%a.x,self.y%a.y,self.z%a.z)
    def rsqrt(self):
        self = Vector3(math.sqrt(self.x),math.sqrt(self.y),math.sqrt(self.z))    
    def __rpow__(self,value):
        a = ToVector3(value)        
        self = Vector3(self.x**a.x,self.y**a.y,self.z**a.z) 
    def __eq__(self,arg):
        a = ToVector3(arg)        
        return self.x == a.x and self.y == a.y and self.z == a.z
    def __le__(self,arg):
        a = ToVector3(arg)        
        return self.x <= a.x and self.y <= a.y and self.z <= a.z              
    def __lt__(self,arg):
        a = ToVector3(arg)        
        return self.x < a.x and self.y < a.y and self.z < a.z
    def __ne__(self,arg):
        a = ToVector3(arg)        
        return self.x != a.x and self.y != a.y and self.z != a.z
    def __gt__(self,arg):
        a = ToVector3(arg)        
        return self.x > a.x and self.y > a.y and self.z > a.z              
    def __ge__(self,arg):
        a = ToVector3(arg)        
        return self.x >= a.x and self.y >= a.y and self.z >= a.z
    def oreq(self,arg):
        a = ToVector3(arg)        
        return self.x == a.x or self.y == a.y or self.z == a.z
    def orle(self,arg):
        a = ToVector3(arg)        
        return self.x <= a.x or self.y <= a.y or self.z <= a.z              
    def orlt(self,arg):
        a = ToVector3(arg)        
        return self.x < a.x or self.y < a.y or self.z < a.z
    def orne(self,arg):
        a = ToVector3(arg)        
        return self.x != a.x or self.y != a.y or self.z != a.z
    def orgt(self,arg):
        a = ToVector3(arg)        
        return self.x > a.x or self.y > a.y or self.z > a.z              
    def orge(self,arg):
        a = ToVector3(arg)        
        return self.x >= a.x or self.y >= a.y or self.z >= a.z    
    def steq(self,arg):
        if type(arg) != Vector3:
            raise TypeError("Argument must be type Vector3")     
        return self == arg
    def stle(self,arg):
        if type(arg) != Vector3:
            raise TypeError("Argument must be type Vector3")     
        return self <= arg             
    def stlt(self,arg):
        if type(arg) != Vector3:
            raise TypeError("Argument must be type Vector3")     
        return self < arg  
    def stne(self,arg):
        if type(arg) != Vector3:
            raise TypeError("Argument must be type Vector3")     
        return self != arg
    def stgt(self,arg):
        if type(arg) != Vector3:
            raise TypeError("Argument must be type Vector3")     
        return self > arg           
    def stge(self,arg):
        if type(arg) != Vector3:
            raise TypeError("Argument must be type Vector3")     
        return self >= arg        
    def __iter__(self):
        return iter([self.x,self.y,self.z])
    def __list__(self):
        return [self.x,self.y,self.z]
    def __dict__(self):
        return {"x":self.x,"y":self.y,"z":self.z}
    def __bool__(self):
        if self.x != 0 and self.y != 0 and self.z != 0:
            return True
        return False
    def __tuple__(self):
        return (self.x,self.y,self.z)
    def __float__(self):
        return float(self.x + self.y+ self.z)
    def __int__(self):
        return int(self.x + self.y+self.z)    
    def __str__(self):
        return  f"x:{str(self.x)} y: {str(self.y)} z: {str(self.z)}"      




class Vector4:
    def __init__(self,x:float,y:float,z:float,w:float):
        if type(x) == float or type(x) == int and type(y) == float or type(y) == int and type(z) == float or type(z) == int and type(w) == float or type(w) == int:
            self.x = x
            self.y = y
            self.z = z   
            self.w = w
        else:
            raise ValueError("X,Y,Z and W must be type float or int!")      
    def __abs__(self):
        return Vector4(abs(self.x),abs(self.y),abs(self.z),abs(self.w))  
    def __round__(self,stage):
        return Vector4(round(self.x,stage),round(self.y,stage),round(self.z,stage),round(self.w,stage))
    def __floor__(self):
        return Vector4(math.floor(self.x),math.floor(self.y),math.floor(self.z),math.floor(self.w))  
    def __trunc__(self):
        return Vector4(math.trunc(self.x),math.trunc(self.y),math.trunc(self.z),math.trunc(self.w))    
    def __ceil__(self):
        return Vector4(math.ceil(self.x),math.ceil(self.y),math.ceil(self.z),math.ceil(self.w))  
    def __neg__(self):
        return Vector4(-self.x, -self.y, -self.z, -self.w)
    def __delattr__(self,*args):
        raise TypeError("Delete not allowed!")
    def __lshift__(self,value):
        a = ToVector4(value)
        return Vector4(self.x<<a.x,self.y<<a.y,self.z<<a.z,self.w<<a.w)                      
    def __rshift__(self,value):
        a = ToVector4(value)
        return Vector4(self.x>>a.x,self.y>>a.y,self.z>>a.z,self.w>>a.w)             
    def __invert__(self):
        return Vector4(~self.x,~self.y,~self.z,~self.w)      
    def __or__(self, value):
        a = ToVector4(value)
        return Vector4(self.x|a.x,self.y|a.y,self.z|a.z,self.w|a.w)            
    def __xor__(self, value):
        a = ToVector4(value)
        return Vector4(self.x^a.x,self.y^a.y,self.z^a.z,self.w^a.w)           
    def __and__(self, value):
        a = ToVector4(value)
        return Vector4(self.x&a.x,self.y&a.y,self.z&a.z,self.w&a.w)         
    def __rlshift__(self,value):
        a = ToVector4(value)
        self = Vector4(self.x<<a.x,self.y<<a.y,self.z<<a.z,self.w<<a.w)                      
    def __rrshift__(self,value):
        a = ToVector4(value)
        self = Vector4(self.x>>a.x,self.y>>a.y,self.z>>a.z,self.w>>a.w)                
    def __ror__(self, value):
        a = ToVector4(value)
        self = Vector4(self.x|a.x,self.y|a.y,self.z|a.z,self.w|a.w)            
    def __rxor__(self, value):
        a = ToVector4(value)
        self = Vector4(self.x^a.x,self.y^a.y,self.z^a.z,self.w^a.w)           
    def __rand__(self, value):
        a = ToVector4(value)
        self = Vector4(self.x&a.x,self.y&a.y,self.z&a.z,self.w&a.w)  
    def __iter__(self):
        return iter([self.x,self.y,self.z,self.w])
    def __list__(self):
        return [self.x,self.y,self.z,self.w]
    def __dict__(self):
        return {"x":self.x,"y":self.y,"z":self.z,"w":self.w}
    def __bool__(self):
        if self.x != 0 and self.y != 0 and self.z != 0 and self.w != 0:
            return True
        return False
    def __tuple__(self):
        return (self.x,self.y,self.z,self.w)
    def __float__(self):
        return float(self.x + self.y+ self.z+ self.w)
    def __int__(self):
        return int(self.x + self.y+self.z+self.w)    
    def __str__(self):
        return  f"x:{str(self.x)} y: {str(self.y)} z: {str(self.z)} w: {str(self.w)}"     
    def __add__(self,arg):
        a = ToVector4(arg)
        return Vector4(self.x+a.x,self.y+a.y,self.z+a.z,self.w+a.w)
    def __sub__(self,arg):
        a = ToVector4(arg)
        return Vector4(self.x-a.x,self.y-a.y,self.z-a.z,self.w-a.w)
    def __mul__(self,arg):
        a = ToVector4(arg)
        return Vector4(self.x*a.x,self.y*a.y,self.z*a.z,self.w*a.zw)
    def __div__(self,arg):
        a = ToVector4(arg)
        return Vector4(self.x/a.x,self.y/a.y,self.z/a.z,self.w/a.w)
    def __truediv__(self,arg):
        return self.__div__(arg)
    def __floordiv__(self,arg):
        return math.floor(self.__div__(arg))   
    def __mod__(self,arg):
        a = ToVector4(arg)        
        return Vector4(self.x%a.x,self.y%a.y,self.z%a.z,self.w%a.w)
    def sqrt(self):
         return Vector4(math.sqrt(self.x),math.sqrt(self.y),math.sqrt(self.z),math.sqrt(self.w))    
    def __pow__(self,value):
        a = ToVector4(value)        
        return Vector4(self.x**a.x,self.y**a.y,self.z**a.z,self.w**a.w)  
    def __radd__(self,arg):
        a = ToVector4(arg)
        self = Vector4(self.x+a.x,self.y+a.y,self.z+a.z,self.w+a.w)
    def __rsub__(self,arg):
        a = ToVector4(arg)
        self =  Vector4(self.x-a.x,self.y-a.y,self.z-a.z,self.w-a.w)
    def __rmul__(self,arg):
        a = ToVector4(arg)
        self = Vector4(self.x*a.x,self.y*a.y,self.z*a.z,self.w*a.w)
    def __rdiv__(self,arg):
        a = ToVector4(arg)
        self = Vector4(self.x/a.x,self.y/a.y,self.z/a.z,self.w/a.w) 
    def __rmod__(self,arg):
        a = ToVector4(arg)        
        self = Vector4(self.x%a.x,self.y%a.y,self.z%a.z,self.w%a.w)
    def rsqrt(self):
        self = Vector4(math.sqrt(self.x),math.sqrt(self.y),math.sqrt(self.z),math.sqrt(self.w))    
    def __rpow__(self,value):
        a = ToVector4(value)        
        self = Vector4(self.x**a.x,self.y**a.y,self.z**a.z,self.w**a.w) 
    def __eq__(self,arg):
        a = ToVector4(arg)        
        return self.x == a.x and self.y == a.y and self.z == a.z and self.w == a.w
    def __le__(self,arg):
        a = ToVector4(arg)        
        return self.x <= a.x and self.y <= a.y and self.z <= a.z  and self.w <= a.w           
    def __lt__(self,arg):
        a = ToVector4(arg)        
        return self.x < a.x and self.y < a.y and self.z < a.z and self.w < a.w
    def __ne__(self,arg):
        a = ToVector4(arg)        
        return self.x != a.x and self.y != a.y and self.z != a.z and self.w != a.w
    def __gt__(self,arg):
        a = ToVector4(arg)        
        return self.x > a.x and self.y > a.y and self.z > a.z  and self.w > a.w           
    def __ge__(self,arg):
        a = ToVector4(arg)        
        return self.x >= a.x and self.y >= a.y and self.z >= a.z and self.w >= a.w
    def oreq(self,arg):
        a = ToVector4(arg)        
        return self.x == a.x or self.y == a.y or self.z == a.z or self.w == a.w
    def orle(self,arg):
        a = ToVector4(arg)        
        return self.x <= a.x or self.y <= a.y or self.z <= a.z or self.w <= a.w             
    def orlt(self,arg):
        a = ToVector4(arg)        
        return self.x < a.x or self.y < a.y or self.z < a.z or self.w < a.w
    def orne(self,arg):
        a = ToVector4(arg)        
        return self.x != a.x or self.y != a.y or self.z != a.z or self.w != a.w
    def orgt(self,arg):
        a = ToVector4(arg)        
        return self.x > a.x or self.y > a.y or self.z > a.z or self.w > a.w           
    def orge(self,arg):
        a = ToVector4(arg)        
        return self.x >= a.x or self.y >= a.y or self.z >= a.z  or self.w >= a.w  
    def steq(self,arg):
        if type(arg) != Vector4:
            raise TypeError("Argument must be type Vector4")     
        return self == arg
    def stle(self,arg):
        if type(arg) != Vector4:
            raise TypeError("Argument must be type Vector4")     
        return self <= arg             
    def stlt(self,arg):
        if type(arg) != Vector4:
            raise TypeError("Argument must be type Vector4")     
        return self < arg  
    def stne(self,arg):
        if type(arg) != Vector4:
            raise TypeError("Argument must be type Vector4")     
        return self != arg
    def stgt(self,arg):
        if type(arg) != Vector4:
            raise TypeError("Argument must be type Vector4")     
        return self > arg           
    def stge(self,arg):
        if type(arg) != Vector4:
            raise TypeError("Argument must be type Vector4")     
        return self >= arg  
        
    


def ToVector3(arg):
    if type(arg) == list or type(arg) == tuple:
        return Vector3(arg[0],arg[1],arg[2]) 
    elif type(arg) == dict:
        return Vector3(arg["x"],arg["y"],arg["z"],) 
    elif type(arg) == Vector2:
        return Vector3(arg.x,arg.y,0)   
    elif type(arg) == Vector4:
        return Vector3(arg.x,arg.y,arg.z)            
    elif type(arg) == float or type(arg) == int:
        return Vector3(arg,arg,arg) 
    elif type(arg) == Vector3:
        return arg
    raise ValueError("Is type not convertable to Vector3!")
def ToVector2(arg):
    if type(arg) == list or type(arg) == tuple:
        return Vector2(arg[0],arg[1]) 
    elif type(arg) == dict:
        return Vector2(arg["x"],arg["y"]) 
    elif type(arg) == Vector3:
        return Vector2(arg.x,arg.y)   
    elif type(arg) == Vector4:
        return Vector2(arg.x,arg.y)            
    elif type(arg) == float or type(arg) == int:
        return Vector2(arg,arg) 
    elif type(arg) == Vector2:
        return arg  
    raise ValueError("Is type not convertable to Vector2!")
def ToVector4(arg):
    if type(arg) == list or type(arg) == tuple:
        return Vector4(arg[0],arg[1],arg[2],arg[3]) 
    elif type(arg) == dict:
        return Vector4(arg["x"],arg["y"],arg["z"],arg["w"]) 
    elif type(arg) == Vector2:
        return Vector4(arg.x,arg.y,0,0)   
    elif type(arg) == Vector3:
        return Vector4(arg.x,arg.y,arg.z,0)            
    elif type(arg) == float or type(arg) == int:
        return Vector4(arg,arg,arg,arg) 
    elif type(arg) == Vector4:
        return arg
    raise ValueError("Is type not convertable to Vector4!")




















































