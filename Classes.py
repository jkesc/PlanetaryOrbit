# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:53:15 2021

@author: jkescher
"""
class body:
    def __init__(self,mass=0,location=[0,0],force=[0,0],name=''): #initializing stationary planetary object with mass, position and force acting on it
        self.setMass(mass)
        self.setLocation(location)
        self.setForce(force)
        self.setName(name)
#Making set and get methods for the class        
    def getMass(self):
            return self.m
        
    def getLocation(self):
        return self.l
    
    def getForce(self):
        return self.f
    
            
    def getName(self):
        return self.n
    
    def setMass(self,mass):
        self.m=mass
    
    def setLocation(self,location):
        self.l=location
        
    def setForce(self,force):
        self.f=force
        
    def setName(self,name):
        self.n=name
    
    def addForce(self, force):
        self.setForce([self.getForce()[0]+force[0],self.getForce()[1]+force[1]])
        
    def updateLocation(self,l):
        return
    
#expanding on the body class to include velocities    
class planet(body):
    
     def __init__(self,mass=0,location=[0,0],force=[0,0],velocity=[0,0],name=''):
         #super(planet,self).__init__(mass,location,force)
         self.setLocation(location)
         self.setMass(mass)
         self.setVelocity(velocity)
         self.setForce(force)
         self.setName(name)
    
     def setVelocity(self,velocity):
         self.v=velocity
        
     def getVelocity(self):
         return self.v

#calculating acceleration in x and y dirn, to update the velocity, to update the location
     def updateLocation(self,dt):
        a=[self.f[0]/self.m,self.f[1]/self.m]
        self.setVelocity([self.getVelocity()[0]+a[0]*dt,self.getVelocity()[1]+a[1]*dt])
        self.setLocation([self.getLocation()[0]+self.getVelocity()[0]*dt,self.getLocation()[1]+self.getVelocity()[1]*dt])
         
#Solar system class to compute interaction between planets
class solarSystem():
    def __init__(self,planets=[],gamma=6.67408e-11,dt=0.1):
        self.p=planets#list with all planets in the system
        self.gamma=gamma #=6.67408e-11[m^3kg^-1s^-2] is the universal gravity constant
        self.dt=dt
    
    def drawSystem(self):#plots all planets
        import matplotlib.pyplot as plt
        leg=[]
        for i in self.p:
            plt.plot(i.getLocation()[0],i.getLocation()[1],'o')
            leg.append(i.getName()[0])
        
        plt.axis('equal')
        plt.ylim([-4.5e12,4.5e12])
        plt.xlim([-4.5e12,4.5e12]) 
        #plt.legend(leg)       
        plt.show()
            
    def addPlanets(self,planets):#adds a new planet (playing god, eh?)
        for i in planets:
            self.p.append(i)
        
    def getPlanets(self):
        return self.p
    
    def gravitationalForce(self,b1,b2): #calculates gravitational force between two planets
        r=self.getDistance(b1,b2)
        dirn=self.getDirection(b1, b2)
        F=self.gamma*b1.getMass()*b2.getMass()/r**2
        return([dirn[0]*F,dirn[1]*F])
        
    def getDistance(self,b1,b2):#distance between two planets
        r=((b2.getLocation()[0]-b1.getLocation()[0])**2+(b2.getLocation()[1]-b1.getLocation()[1])**2)**(1/2)
        if r==0:
            r=7./3 - 4./3 -1#returns machine epsilon in case r=0, to avoid division by 0
            
        return r
        
    
    def getDirection(self,b1,b2):#direction between two planets, normalized
        dirn=[0,0]
        r=self.getDistance(b1,b2)
        for i in range(2):

            dirn[i]=(b2.getLocation()[i]-b1.getLocation()[i])/r
        return dirn
        
    def updateSystem(self): #calculates next step for all planets
        for i in self.p:
            i.setForce([0,0])
            for j in self.p:
                if not(i == j):
                    i.addForce(self.gravitationalForce(i, j))
        for i in self.p:
            i.updateLocation(self.dt)    
    
        
def main():
    import time
    sun=body(1.989e30,[0,0],[0,0],name='Sol')
    mercury=planet(3.3011e23,[57909050e3,0],[0,0],[0,47.9e3],name='Mercury')#mass, location, force, velocity
    venus=planet(4.8675e24,[108208e6,0],[0,0],[0,35e3],name='Venus')#mass, location, force, velocity
    earth=planet(5.972e24,[149598023e3,0],[0,0],[0,29.8e3],name='Earth')#mass, location, force, velocity
    mars=planet(64171e23,[227939200e3,0],[0,0],[0,24.1e3],name='Mars')#mass, location, force, velocity
    jupiter=planet(1.8982e27,[778.57e9,0],[0,0],[0,13.1e3],name='Jupiter')#mass, location, force, velocity
    saturn=planet(5.6834e26,[1455.53e9,0],[0,0],[0,9.7e3],name='Saturn')#mass, location, force, velocity
    uranus=planet(8.6810e25,[2875.04e9,0],[0,0],[0,6.8e3],name='Uranus')#mass, location, force, velocity
    neptune=planet(1.02413e26,[4.5e12,0],[0,0],[0,5.4e3],name='Neptune')#mass, location, force, velocity
    syst=solarSystem([sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,],dt=86400)
    while True:
        time.sleep(0.2)
        syst.drawSystem()
        syst.updateSystem()
    
if __name__=="__main__":
    main()