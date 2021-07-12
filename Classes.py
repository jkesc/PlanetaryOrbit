# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:53:15 2021

@author: jkescher
"""
class body:
    def __init__(self,mass=0,location=[0,0],force[0,0]):
        self.setMass(mass)
        self.setLocation(location)
        
    def getMass(self):
            return self.m
        
    def getLocation(self):
        return self.l
    
    def getForce(self)
    
    def setMass(self,mass):
        self.m=mass
    
    def setLocation(self,location):
        self.l=location
        
    def setForce(self,force):
        self.f=force
        
    def updateLocation(l):
        return
        
        
class planet(body):
    
     def __init__(self,mass=0,location=[0,0],force[0,0],velocity=[0,0]):
         super(planet,self).__init__(mass,location,force)
         self.setLocation(location)
    
     def setVelocity(self,velocity):
         self.v=velocity
        
     def getVelocity(self):
         return self.v
        
     def updateLocation(self,l):
         setLocation(l)
         
class solarSystem():
    self.gamma=6.67408e-11 #[m^3kg^-1s^-2] universal gravity constant
    def __init__(self,planets=[]):
        self.p=planets
    
    def drawSystem(self):
        import matplotlib.pyplot as plt
        for i in self.p:
            plt.plot(i.getLocation[0],i.getLocation[1],'o')
            
        plt.show()
            
    def addPlanets(self,planets):
        self.p.append(planets)
    
    def gravitaionalForce(self,b1,b2):
        r=self.getDistance(b1,b2)
        F=self.gamma*b1.getMass()*b2.getMass()/r**2
    def getDistance(self,b1,b2):
        return ((b1.getLocation[0]-b2.getLocation[0])**2+(b1.getLocation[1]-b2.getLocation[1])**2)**(1/2)
        
        
def main():
    x=planet(0,[1,0],[0,0])
    y=planet((0,[2,0],[0,0]))
    z=planet(0,[0,2],[0,0])
    
    syst=solarSystem([x,y,z])
    syst.drawSystem()
    
    
if __name__=="__main__":
    main()