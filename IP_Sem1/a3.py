import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.A=A
        self.A_copy=A.copy()

        
 
    
    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        self.A_copy=self.A.copy()
        super().translate(dx , dy)
        for i in range(len(self.A)):
            self.A[i] = list(np.matmul(self.T_t , self.A[i]))
        final_cord_x=[]
        final_cord_y=[]
        for i in range(len(self.A)):
            # self.A[i] = list(np.matmul(self.T_t , self.A[i]))
            final_cord_x.append(round(self.A[i][0] , 2))
            final_cord_y.append(round(self.A[i][1] , 2))
        return (final_cord_x , final_cord_y)


    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        
        self.A_copy=self.A.copy()
        # self.final_coord_x=[]
        # self.final_coord_y=[]
        
        centroid_x=0
        centroid_y=0
        for i in range(len(self.A)):
            centroid_x += self.A[i][0]/len(self.A)
            centroid_y += self.A[i][1]/len(self.A)
        super().translate(-centroid_x , -centroid_y)
        for i in range(len(self.A)):
            self.A[i] = list(np.matmul(self.T_t , self.A[i]))
        super().scale(sx , sy)
        for i in range(len(self.A)):
            self.A[i] = list(np.matmul(self.T_s , self.A[i]))
        
        super().translate(centroid_x , centroid_y)
        for i in range(len(self.A)):
            self.A[i] = list(np.matmul(self.T_t , self.A[i]))
        final_coord_x=[]
        final_coord_y=[]
        
        for j in range(len(self.A)):
            final_coord_x.append(round(self.A[j][0] , 2))
            final_coord_y.append(round(self.A[j][1] , 2))
        return (final_coord_x ,final_coord_y)

 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
       
        self.A_copy=self.A.copy()
        # self.final_coord_x=[]
        # self.final_coord_y=[]
        
        
        super().translate(-rx , -ry)
        for i in range(len(self.A)):
            self.A[i] = list(np.matmul(self.T_t , self.A[i]))
        super().rotate(deg)
        for i in range(len(self.A)):
            self.A[i] = list(np.matmul(self.T_r , self.A[i]))
        
        super().translate(rx , ry)
        for i in range(len(self.A)):
            self.A[i] = list(np.matmul(self.T_t , self.A[i]))
        final_coord_x=[]
        final_coord_y=[]
        
        for j in range(len(self.A)):
            final_coord_x.append(round(self.A[j][0] , 2))
            final_coord_y.append(round(self.A[j][1] , 2))
        return (final_coord_x ,final_coord_y)

    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        
        self.final_coord_x_copy=[]
        self.final_coord_y_copy=[]
        
        self.final_coord_x=[]
        self.final_coord_y=[]
        
        for j in range(len(self.A)):
            self.final_coord_x.append(round(self.A[j][0] , 2))
            self.final_coord_y.append(round(self.A[j][1] , 2))
        for j in range(len(self.A_copy)):
            self.final_coord_x_copy.append(round(self.A_copy[j][0] , 2))
            self.final_coord_y_copy.append(round(self.A_copy[j][1] , 2))
        self.final_coord_x_copy.append(self.final_coord_x_copy[0])
        self.final_coord_y_copy.append(self.final_coord_y_copy[0])
        self.final_coord_x.append(self.final_coord_x[0])
        self.final_coord_y.append(self.final_coord_y[0])
        plt.plot(np.array(self.final_coord_x_copy) , np.array(self.final_coord_y_copy) , ls = "dashed")
        plt.plot(np.array(self.final_coord_x) , np.array(self.final_coord_y))
        x_dim=max(max(self.final_coord_x) , max(self.final_coord_x_copy))
        y_dim=max(max(self.final_coord_y) , max(self.final_coord_y_copy))
        Shape.plot(self , int(x_dim) , int(y_dim))

class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.circle_x=x
        self.circle_x_copy=x
        self.circle_y=y
        self.circle_y_copy=y
        self.circle_radius=radius
        self.circle_radius_copy=radius
        self.circle_matrix=np.array([self.circle_x , self.circle_y , 1])
        

    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        super().translate(dx , dy)
        self.circle_x_copy=self.circle_x
        self.circle_y_copy=self.circle_y
        self.circle_radius_copy=self.circle_radius
        self.circle_matrix=np.matmul(self.T_t , self.circle_matrix)
        self.circle_x=round(self.circle_matrix[0] , 2)
        self.circle_y=round(self.circle_matrix[1],2)
        return [self.circle_x,self.circle_y  , self.circle_radius]
        
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        #self.sy=None
        super().scale(sx , 0)
        self.circle_x_copy=self.circle_x
        self.circle_y_copy=self.circle_y
        self.circle_radius_copy=self.circle_radius
        self.circle_radius=(self.T_s[0][0]*self.circle_radius)
        return [self.circle_x,self.circle_y  , round(self.circle_radius , 2)]
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.circle_x_copy=self.circle_x
        self.circle_y_copy=self.circle_y
        self.circle_radius_copy=self.circle_radius
        # self.rx=rx
        # self.ry=ry
        super().rotate(deg)
        
        
        super().translate(-rx , -ry)
        self.circle_matrix=np.matmul(self.T_t , self.circle_matrix)
        self.circle_matrix=np.matmul(self.T_r ,self.circle_matrix )
        super().translate(rx , ry)
        self.circle_matrix=np.matmul(self.T_t , self.circle_matrix)
        self.circle_x=round(self.circle_matrix[0] , 2)
        self.circle_y=round(self.circle_matrix[1] , 2 )
        return [self.circle_x,self.circle_y  , self.circle_radius]
        
 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        
        cir1=plt.Circle( (self.circle_x_copy , self.circle_y_copy) , self.circle_radius_copy , fill=None ,ls="dashed")
        cir2=plt.Circle((self.circle_x , self.circle_y) , self.circle_radius , fill=None)
        a1=plt.gca()
        a1.add_patch(cir1)
        
        # a1=plt.gca()
        a1.add_patch(cir2)
        super().plot(max(max(self.circle_x_copy , self.circle_y_copy) + self.circle_radius_copy , max(self.circle_x , self.circle_y)+self.circle_radius),max(max(self.circle_x_copy , self.circle_y_copy) + self.circle_radius_copy , max(self.circle_x , self.circle_y)+self.circle_radius))
        
        

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    
    verbose=int(input("1 to plot, 0 otherwise: "))
    t=int(input("Enter Number of Test Cases : "))
    for test in range(t):
        shape=int(input("Enter type of shape (polygon = 0 /circle = 1) : "))
        if shape==0:
            A=[]
            x_initial=[]
            y_initial=[]
            sides=int(input("Enter Number of Sides : "))
            for i in range(sides):
                x,y=input(f"Enter x{i} , y{i} : ").split()
                A.append([float(x) , float(y) , float(1)])
                
                x_initial.append(x)
                y_initial.append(y)
            query=int(input("Enter the number of queries : "))
            sample=Polygon(A)
            # sample_copy_x=Polygon(A)
            # sample_copy_y=Polygon(A)
            if verbose==1:
                for j in range(query):
                    type_query=input("Enter Query : ")
                    if type_query[0]=='R':
                        try:
                            R , deg , rx , ry = type_query.split()
                        except:
                            R , deg = type_query.split()
                            rx=0
                            ry=0


                        print(x_initial , y_initial)
                        print(sample.rotate(float(deg) , float(rx) , float(ry)))
                        # x_initial=sample.rotate(deg , rx , ry)[0]
                        # y_initial=sample.rotate(deg , rx , ry)[1]
                        sample.plot()
                    elif type_query[0]=='T':
                        try:
                            T , dx , dy = type_query.split()
                        except:
                            T , dx = type_query.split()
                            dy=dx
                        print(x_initial , y_initial)
                        # y_initial=sample.translate(float(dx) , float(dy))[1]
                        # x_initial=sample.translate(float(dx) , float(dy))[0]
                        print(sample.translate(float(dx) , float(dy)))
                        sample.plot()
                    elif type_query[0]=='S':
                        try:
                            T , sx , sy = type_query.split()
                        except:
                            T , sx = type_query.split()
                            sy=sx
                        print(x_initial , y_initial)
                        print(sample.scale(float(sx) , float(sy)))
                        sample.plot()
                    elif type_query[0]=='P':
                        sample.plot()
            else:
                for j in range(query):
                    type_query=input("Enter Query : ")
                    if type_query[0]=='R':
                        try:
                            R , deg , rx , ry = type_query.split()
                        except:
                            R , deg = type_query.split()
                            rx=0
                            ry=0
                        
                        

                        print(x_initial , y_initial)
                        
                        print(sample.rotate(float(deg) , float(rx) , float(ry)))
                        # x_initial=sample_copy_x.rotate(float(deg) , float(rx) , float(ry))[0]
                        # y_initial=sample_copy_y.rotate(float(deg) , float(rx) , float(ry))[1]
                    elif type_query[0]=='T':
                        try:
                            T , dx , dy = type_query.split()
                        except:
                            T , dx = type_query.split()
                            dy=dx
                        print(x_initial , y_initial)
                        
                        print(sample.translate(float(dx) , float(dy)))
                        # x_initial=sample_copy_x.translate(float(dx) , float(dy))[0]
                        # y_initial=sample_copy_y.translate(float(dx) , float(dy))[1]

                    elif type_query[0]=='S':
                        try:
                            T , sx , sy = type_query.split()
                        except:
                            T , sx = type_query.split()
                            sy=sx
                        print(x_initial , y_initial)
                        
                        print(sample.scale(float(sx) , float(sy)))
                        # x_initial=sample_copy_x.scale(float(sx) , float(sy))[0]
                        # y_initial=sample_copy_y.scale(float(sx) , float(sy))[1]
                    elif type_query[0]=='P':
                        sample.plot()

        if shape==1:
            # A=[]
            # x_initial=[]
            # y_initial=[]
            # sides=int(input("Enter Number of Sides : "))
            # for i in range(sides):
            #     x,y=input(f"Enter x{i} , y{i} : ").split()
            #     A.append([float(x) , float(y) , float(1)])
                
            #     x_initial.append(x)
            #     y_initial.append(y)
            x=float(input("Enter X coord Of Circle : "))
            y=float(input("Enter X coord Of Circle : "))
            radius=float(input("Enter Radius : "))
            query=int(input("Enter the number of queries : "))
            csample=Circle(x , y , radius)
            if verbose==1:
                for j in range(query):
                    type_query=input("Enter Query : ")
                    if type_query[0]=='R':
                        try:
                            R , deg , rx , ry = type_query.split()
                        except:
                            R , deg = type_query.split()
                            rx=0
                            ry=0


                        # print(x_initial , y_initial)
                        print(csample.rotate(float(deg) , float(rx) , float(ry)))
                        csample.plot()
                        # x_initial=sample.rotate(deg , rx , ry)[0]
                        # y_initial=sample.rotate(deg , rx , ry)[1]
                    elif type_query[0]=='T':
                        try:
                            T , dx , dy = type_query.split()
                        except:
                            T , dx = type_query.split()
                            dy=dx
                        # print(x_initial , y_initial)
                        # y_initial=sample.translate(float(dx) , float(dy))[1]
                        # x_initial=sample.translate(float(dx) , float(dy))[0]
                        print(csample.translate(float(dx) , float(dy)))
                        csample.plot()
                    elif type_query[0]=='S':

                        T , sx = type_query.split()

                        # print(x_initial , y_initial)
                        print(csample.scale(float(sx)))
                        csample.plot()
                    elif type_query[0]=='P':
                        csample.plot()
            else:
                for j in range(query):
                    type_query=input("Enter Query : ")
                    if type_query[0]=='R':
                        try:
                            R , deg , rx , ry = type_query.split()
                        except:
                            R , deg = type_query.split()
                            rx=0
                            ry=0


                        # print(x_initial , y_initial)
                        print(csample.rotate(float(deg) , float(rx) , float(ry)))
                        # x_initial=sample.rotate(deg , rx , ry)[0]
                        # y_initial=sample.rotate(deg , rx , ry)[1]
                    elif type_query[0]=='T':
                        try:
                            T , dx , dy = type_query.split()
                        except:
                            T , dx = type_query.split()
                            dy=dx
                        # print(x_initial , y_initial)
                        # y_initial=sample.translate(float(dx) , float(dy))[1]
                        # x_initial=sample.translate(float(dx) , float(dy))[0]
                        print(csample.translate(float(dx) , float(dy)))

                    elif type_query[0]=='S':

                        T , sx = type_query.split()

                        # print(x_initial , y_initial)
                        print(csample.scale(float(sx)))
                    elif type_query[0]=='P':
                        csample.plot()
                        # print(csample.scale(float(sx) , float(sy)))




    


