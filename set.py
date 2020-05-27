"""
Filename: set.py
Username: Walsha
Date: May 16
"""

import graphics
import random

window = graphics.GraphWin("Set", 750, 500)
window.setBackground('white')


                               
class card: 
    """
    creates a card with attribues symbol, color, fill_level, and amount all random
    """
    
    def __init__(self, point, width, height): 
        """
        constructor: creates a card object of given width and height with 4 different unique attributes, symbol, amount, color, and fill. (all random)
        Parameters:
            self
            point: center point location of object
            width: width of card
            height: height of card
        """
   
        self.point = point
        p1 = graphics.Point(point.getX() - width / 2, point.getY() - height / 2)
        p2 = graphics.Point(point.getX() + width / 2, point.getY() + height / 2)
        self.rect = graphics.Rectangle(p1, p2)
        self.rect.draw(window)
        
        odds_amount = random.randrange(0,3)
        if odds_amount == 0:
            self.amount = 1
        elif odds_amount == 1:
            self.amount = 2
        elif odds_amount == 2:
            self.amount = 3
        
        odds_symbol = random.randrange(0,3)
        if odds_symbol == 0:
            self.symbol = 'diamond'
        elif odds_symbol == 1:
            self.symbol = 'oval'
        elif odds_symbol == 2:
            self.symbol = 'squiggle'
        
        odds_color = random.randrange(0,3)
        if odds_color == 0:
            self.color = 'purple'
        elif odds_color == 1:
            self.color = 'red'
        elif odds_color == 2:
            self.color = 'green'
            
        odds_type = random.randrange(0,3)
        if odds_type == 0:
            self.type = 'solid'
        elif odds_type == 1:
            self.type = 'stripped'
        elif odds_type == 2:
            self.type = 'blank'
            
    def wasClicked(self, point):
        """
        Returns true if given card object was clicked and false if it was not
        Parameters:
            self
            point: location of card
        """
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        if (p1.getX() <= point.getX() <= p2.getX() and
            p1.getY() <= point.getY() <= p2.getY()):
            return True
        return False
    
    def getinfo(self):
        """
        Returns a list of attributes of a certain card
        Parameters:
            self
        """
        attlist = [self.amount, self.symbol, self.color, self.type]
        return attlist
        
            
    def squiggle(self, point):
        """
        Draws the squiggle shape on the card, draws either 1, 2 or 3 of them, either green, purple or red, with either solid, stripped or blank fill. 
        Parameters:
            self
            point: location of card
        """
        
        s1 = graphics.Point(point.getX() + 10, point.getY() + 30)
        s2 = graphics.Point(point.getX() - 10, point.getY() + 10)
        s3 = graphics.Point(point.getX() , point.getY() - 5)
        s4 = graphics.Point(point.getX() - 10, point.getY() - 25)
        s5 = graphics.Point(point.getX() + 10, point.getY() - 5)
        s6 = graphics.Point(point.getX() , point.getY() + 10)
        
        if self.amount == 1:
            s1 = graphics.Point(point.getX() + 10, point.getY() + 30)
            s2 = graphics.Point(point.getX() - 10, point.getY() + 10)
            s3 = graphics.Point(point.getX() , point.getY() - 5)
            s4 = graphics.Point(point.getX() - 10, point.getY() - 25)
            s5 = graphics.Point(point.getX() + 10, point.getY() - 5)
            s6 = graphics.Point(point.getX() , point.getY() + 10)
            
            if self.type == 'solid':
                if self.color == 'purple':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setOutline('purple')
                    squiggle1.setFill('purple')
                    squiggle1.draw(window)
                elif self.color == 'red':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setOutline('red')
                    squiggle1.setFill('red')
                    squiggle1.draw(window)
                elif self.color == 'green':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setOutline('green')
                    squiggle1.setFill('green')
                    squiggle1.draw(window)
                    
            elif self.type == 'stripped':
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                if self.color == 'purple':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setFill('purple')
                    squiggle1.setOutline('purple')
                    squiggle1.draw(window)
                    
                elif self.color == 'red':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setFill('red')
                    squiggle1.setOutline('red')
                    squiggle1.draw(window)
                    
                elif self.color == 'green':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setFill('green')
                    squiggle1.setOutline('green')
                    squiggle1.draw(window)
                    
                for i in range(22): #draw lines
                        line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                        line.setOutline('white')
                        line.draw(window)
                        p1y = p1y + 3
                        p2y = p2y + 3
                
            elif self.type == 'blank':
                if self.color == 'purple':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setOutline('purple')
                    squiggle1.draw(window)
                elif self.color == 'red':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setOutline('red')
                    squiggle1.draw(window)
                elif self.color == 'green':
                    squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
                    squiggle1.setOutline('green')
                    squiggle1.draw(window)

            
            
        elif self.amount == 2:
            
            s1 = graphics.Point(point.getX() + 30, point.getY() + 30)
            s2 = graphics.Point(point.getX() + 10, point.getY() + 10)
            s3 = graphics.Point(point.getX() + 20 , point.getY() - 5)
            s4 = graphics.Point(point.getX() + 10, point.getY() - 25)
            s5 = graphics.Point(point.getX() + 30, point.getY() - 5)
            s6 = graphics.Point(point.getX() + 20 , point.getY() + 10)
            squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
            
            s1 = graphics.Point(point.getX() - 10, point.getY() + 30)
            s2 = graphics.Point(point.getX() - 30, point.getY() + 10)
            s3 = graphics.Point(point.getX() - 20 , point.getY() - 5)
            s4 = graphics.Point(point.getX() - 30, point.getY() - 25)
            s5 = graphics.Point(point.getX() - 10, point.getY() - 5)
            s6 = graphics.Point(point.getX() - 20, point.getY() + 10)
            squiggle2 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
            
            
            if self.type == 'solid':
                if self.color == 'purple':
                    squiggle1.setOutline('purple')
                    squiggle1.setFill('purple')
                    squiggle1.draw(window)
                    squiggle2.setOutline('purple')
                    squiggle2.setFill('purple')
                    squiggle2.draw(window)
                elif self.color == 'red':
                    squiggle1.setOutline('red')
                    squiggle1.setFill('red')
                    squiggle1.draw(window)
                    squiggle2.setOutline('red')
                    squiggle2.setFill('red')
                    squiggle2.draw(window)
                elif self.color == 'green':
                    squiggle1.setOutline('green')
                    squiggle1.setFill('green')
                    squiggle1.draw(window)
                    squiggle2.setOutline('green')
                    squiggle2.setFill('green')
                    squiggle2.draw(window)
                    
            elif self.type == 'stripped':
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                if self.color == 'purple':
                    squiggle1.setFill('purple')
                    squiggle1.setOutline('purple')
                    squiggle1.draw(window)
                    squiggle2.setOutline('purple')
                    squiggle2.setFill('purple')
                    squiggle2.draw(window)
                        
                elif self.color == 'red':
                    squiggle1.setFill('red')
                    squiggle1.setOutline('red')
                    squiggle1.draw(window)
                    squiggle2.setFill('red')
                    squiggle2.setOutline('red')
                    squiggle2.draw(window)
                    
                elif self.color == 'green':
                    squiggle1.setFill('green')
                    squiggle1.setOutline('green')
                    squiggle1.draw(window)
                    squiggle2.setOutline('green')
                    squiggle2.setFill('green')
                    squiggle2.draw(window)
                    
                for i in range(22):
                        line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                        line.setOutline('white')
                        line.draw(window)
                        p1y = p1y + 3
                        p2y = p2y + 3
                        
            elif self.type == 'blank':
                if self.color == 'purple':
                    squiggle1.setOutline('purple')
                    squiggle1.draw(window)
                    squiggle2.setOutline('purple')
                    squiggle2.draw(window)
                elif self.color == 'red':
                    squiggle1.setOutline('red')
                    squiggle1.draw(window)
                    squiggle2.setOutline('red')
                    squiggle2.draw(window)
                elif self.color == 'green':
                    squiggle1.setOutline('green')
                    squiggle1.draw(window)
                    squiggle2.setOutline('green')
                    squiggle2.draw(window)
        
        elif self.amount == 3:
            s1 = graphics.Point(point.getX() + 10, point.getY() + 30)
            s2 = graphics.Point(point.getX() - 10, point.getY() + 10)
            s3 = graphics.Point(point.getX() , point.getY() - 5)
            s4 = graphics.Point(point.getX() - 10, point.getY() - 25)
            s5 = graphics.Point(point.getX() + 10, point.getY() - 5)
            s6 = graphics.Point(point.getX() , point.getY() + 10)
            squiggle1 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
            outsqu = squiggle1
            
            s1 = graphics.Point(point.getX() + 40, point.getY() + 30) # + 20
            s2 = graphics.Point(point.getX() + 20, point.getY() + 10)
            s3 = graphics.Point(point.getX() + 30 , point.getY() - 5)
            s4 = graphics.Point(point.getX() + 20, point.getY() - 25)
            s5 = graphics.Point(point.getX() + 40, point.getY() - 5)
            s6 = graphics.Point(point.getX() + 30 , point.getY() + 10)
            squiggle2 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
            outsqu2 = squiggle2
           
            s1 = graphics.Point(point.getX() - 20, point.getY() + 30) # -20
            s2 = graphics.Point(point.getX() - 40, point.getY() + 10)
            s3 = graphics.Point(point.getX() - 30 , point.getY() - 5)
            s4 = graphics.Point(point.getX() - 40, point.getY() - 25)
            s5 = graphics.Point(point.getX() - 20, point.getY() - 5)
            s6 = graphics.Point(point.getX() - 30, point.getY() + 10)
            squiggle3 = graphics.Polygon(s1, s2, s3, s4, s5, s6)
            outsqu3 = squiggle3
            
            
            if self.type == 'solid':
                if self.color == 'purple':
                    squiggle1.setOutline('purple')
                    squiggle1.setFill('purple')
                    squiggle1.draw(window)
                    squiggle2.setOutline('purple')
                    squiggle2.setFill('purple')
                    squiggle2.draw(window)
                    squiggle3.setOutline('purple')
                    squiggle3.setFill('purple')
                    squiggle3.draw(window)
                elif self.color == 'red':
                    squiggle1.setOutline('red')
                    squiggle1.setFill('red')
                    squiggle1.draw(window)
                    squiggle2.setOutline('red')
                    squiggle2.setFill('red')
                    squiggle2.draw(window)
                    squiggle3.setOutline('red')
                    squiggle3.setFill('red')
                    squiggle3.draw(window)
                elif self.color == 'green':
                    squiggle1.setOutline('green')
                    squiggle1.setFill('green')
                    squiggle1.draw(window)
                    squiggle2.setOutline('green')
                    squiggle2.setFill('green')
                    squiggle2.draw(window)
                    squiggle3.setOutline('green')
                    squiggle3.setFill('green')
                    squiggle3.draw(window)
                    
            elif self.type == 'stripped':
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                if self.color == 'purple':
                    squiggle1.setFill('purple')
                    squiggle1.setOutline('purple')
                    squiggle1.draw(window)
                    squiggle2.setFill('purple')
                    squiggle2.setOutline('purple')
                    squiggle2.draw(window)
                    squiggle3.setFill('purple')
                    squiggle3.setOutline('purple')
                    squiggle3.draw(window)
                    
                elif self.color == 'red':
                    squiggle1.setFill('red')
                    squiggle1.setOutline('red')
                    squiggle1.draw(window)
                    squiggle2.setFill('red')
                    squiggle2.setOutline('red')
                    squiggle2.draw(window)
                    squiggle3.setFill('red')
                    squiggle3.setOutline('red')
                    squiggle3.draw(window)
                    
                elif self.color == 'green':
                    squiggle1.setFill('green')
                    squiggle1.setOutline('green')
                    squiggle1.draw(window)
                    squiggle2.setFill('green')
                    squiggle2.setOutline('green')
                    squiggle2.draw(window)
                    squiggle3.setFill('green')
                    squiggle3.setOutline('green')
                    squiggle3.draw(window)
                    
                for i in range(22):
                        line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                        line.setOutline('white')
                        line.draw(window)
                        p1y = p1y + 3
                        p2y = p2y + 3
                        
                        
            elif self.type == 'blank':
                if self.color == 'purple':
                    squiggle1.setOutline('purple')
                    squiggle1.draw(window)
                    squiggle2.setOutline('purple')
                    squiggle2.draw(window)
                    squiggle3.setOutline('purple')
                    squiggle3.draw(window)
                elif self.color == 'red':
                    squiggle1.setOutline('red')
                    squiggle1.draw(window)
                    squiggle2.setOutline('red')
                    squiggle2.draw(window)
                    squiggle3.setOutline('red')
                    squiggle3.draw(window)
                elif self.color == 'green':
                    squiggle1.setOutline('green')
                    squiggle1.draw(window)
                    squiggle2.setOutline('green')
                    squiggle2.draw(window)
                    squiggle3.setOutline('green')
                    squiggle3.draw(window)
        
        
        
    def oval(self, point):
        """
        Draws the oval shape on the card, draws either 1, 2 or 3 of them, either green, purple or red, with either solid, stripped or blank fill.
        Parameters:
            self
            point: location of card
        """
        
        if self.amount == 1:
            ovalp1 = graphics.Point(point.getX() - 15, point.getY() + 30)
            ovalp2 = graphics.Point(point.getX() + 15 , point.getY() - 30)
            oval = graphics.Oval(ovalp1, ovalp2)
            
            if self.type == 'solid':
                if self.color == 'purple':
                    oval.setOutline('purple')
                    oval.setFill('purple')
                    oval.draw(window)
                elif self.color == 'red':
                    oval.setFill('red')
                    oval.setOutline('red')
                    oval.draw(window)
                elif self.color == 'green':
                    oval.setFill('green')
                    oval.setOutline('green')
                    oval.draw(window)
                    
            elif self.type == 'stripped':
                if self.color == 'purple':
                    oval.setFill('purple')
                    oval.setOutline('purple')
                    oval.draw(window)
                elif self.color == 'red':
                    oval.setFill('red')
                    oval.setOutline('red')
                    oval.draw(window)
                elif self.color == 'green':
                    oval.setFill('green')
                    oval.setOutline('green')
                    oval.draw(window)
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                for i in range(22):
                    line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                    line.setOutline('white')
                    line.draw(window)
                    p1y = p1y + 3
                    p2y = p2y + 3
                    
            elif self.type == 'blank':
                if self.color == 'purple':
                    oval.setOutline('purple')
                    oval.draw(window)
                elif self.color == 'red':
                    oval.setOutline('red')
                    oval.draw(window)
                elif self.color == 'green':
                    oval.setOutline('green')
                    oval.draw(window)
                
                    
            
        elif self.amount == 2:
            x1 = point.getX() - 15
            y1 = point.getY() + 30
            x2 = point.getX() + 15
            y2 = point.getY() - 30
            ovalp1 = graphics.Point(x1 - 25, y1)
            ovalp2 = graphics.Point(x2 - 25 , y2)
            oval = graphics.Oval(ovalp1, ovalp2)
            ovalp1 = graphics.Point(x1 + 25, y1)
            ovalp2 = graphics.Point(x2 + 25 , y2)
            oval2 = graphics.Oval(ovalp1, ovalp2)
            
            
            if self.type == 'solid':
                if self.color == 'purple':
                    oval.setFill('purple')
                    oval.setOutline('purple')
                    oval.draw(window)
                    oval2.setFill('purple')
                    oval2.setOutline('purple')
                    oval2.draw(window)
                elif self.color == 'red':
                    oval.setFill('red')
                    oval.setOutline('red')
                    oval.draw(window)
                    oval2.setFill('red')
                    oval2.setOutline('red')
                    oval2.draw(window)
                elif self.color == 'green':
                    oval.setFill('green')
                    oval.setOutline('green')
                    oval.draw(window)
                    oval2.setFill('green')
                    oval2.setOutline('green')
                    oval2.draw(window)
                    
            elif self.type == 'stripped':
                if self.color == 'purple':
                    oval.setFill('purple')
                    oval.setOutline('purple')
                    oval.draw(window)
                    oval2.setOutline('purple')
                    oval2.setFill('purple')
                    oval2.draw(window)
                elif self.color == 'red':
                    oval.setFill('red')
                    oval.setOutline('red')
                    oval.draw(window)
                    oval2.setFill('red')
                    oval2.setOutline('red')
                    oval2.draw(window)
                elif self.color == 'green':
                    oval.setFill('green')
                    oval.setOutline('green')
                    oval.draw(window)
                    oval2.setOutline('green')
                    oval2.setFill('green')
                    oval2.draw(window)
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                for i in range(22):
                    line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                    line.setOutline('white')
                    line.draw(window)
                    p1y = p1y + 3
                    p2y = p2y + 3
                    
            elif self.type == 'blank':
                if self.color == 'purple':
                    oval.setOutline('purple')
                    oval.draw(window)
                    oval2.setOutline('purple')
                    oval2.draw(window)
                elif self.color == 'red':
                    oval.setOutline('red')
                    oval.draw(window)
                    oval2.setOutline('red')
                    oval2.draw(window)
                elif self.color == 'green':
                    oval.setOutline('green')
                    oval.draw(window)
                    oval2.setOutline('green')
                    oval2.draw(window)
            
        elif self.amount == 3:
            x1 = point.getX() - 15
            y1 = point.getY() + 30
            x2 = point.getX() + 15
            y2 = point.getY() - 30
            ovalp1 = graphics.Point(x1, y1)
            ovalp2 = graphics.Point(x2, y2)
            oval = graphics.Oval(ovalp1, ovalp2)
            
            ovalp1 = graphics.Point(x1 - 40, y1)
            ovalp2 = graphics.Point(x2 - 40 , y2)
            oval2 = graphics.Oval(ovalp1, ovalp2)
            
            ovalp1 = graphics.Point(x1 + 40, y1)
            ovalp2 = graphics.Point(x2 + 40 , y2)
            oval3 = graphics.Oval(ovalp1, ovalp2)
            
            
            if self.type == 'solid':
                if self.color == 'purple':
                    oval.setFill('purple')
                    oval.setOutline('purple')
                    oval.draw(window)
                    oval2.setFill('purple')
                    oval2.setOutline('purple')
                    oval2.draw(window)
                    oval3.setFill('purple')
                    oval3.setOutline('purple')
                    oval3.draw(window)
                elif self.color == 'red':
                    oval.setFill('red')
                    oval.setOutline('red')
                    oval.draw(window)
                    oval2.setFill('red')
                    oval2.setOutline('red')
                    oval2.draw(window)
                    oval3.setFill('red')
                    oval3.setOutline('red')
                    oval3.draw(window)
                elif self.color == 'green':
                    oval.setFill('green')
                    oval.setOutline('green')
                    oval.draw(window)
                    oval2.setFill('green')
                    oval2.setOutline('green')
                    oval2.draw(window)
                    oval3.setFill('green')
                    oval3.setOutline('green')
                    oval3.draw(window)
                    
            elif self.type == 'stripped':
                if self.color == 'purple':
                    oval.setFill('purple')
                    oval.setOutline('purple')
                    oval.draw(window)
                    oval2.setFill('purple')
                    oval2.setOutline('purple')
                    oval2.draw(window)
                    oval3.setFill('purple')
                    oval3.setOutline('purple')
                    oval3.draw(window)
                elif self.color == 'red':
                    oval.setFill('red')
                    oval.setOutline('red')
                    oval.draw(window)
                    oval2.setFill('red')
                    oval2.setOutline('red')
                    oval2.draw(window)
                    oval3.setOutline('red')
                    oval3.setFill('red')
                    oval3.draw(window)
                elif self.color == 'green':
                    oval.setFill('green')
                    oval.setOutline('green')
                    oval.draw(window)
                    oval2.setFill('green')
                    oval2.setOutline('green')
                    oval2.draw(window)
                    oval3.setOutline('green')
                    oval3.setFill('green')
                    oval3.draw(window)
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                for i in range(22):
                    line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                    line.setOutline('white')
                    line.draw(window)
                    p1y = p1y + 3
                    p2y = p2y + 3
              
            elif self.type == 'blank':
                if self.color == 'purple':
                    oval.setOutline('purple')
                    oval.draw(window)
                    oval2.setOutline('purple')
                    oval2.draw(window)
                    oval3.setOutline('purple')
                    oval3.draw(window)
                elif self.color == 'red':
                    oval.setOutline('red')
                    oval.draw(window)
                    oval2.setOutline('red')
                    oval2.draw(window)
                    oval3.setOutline('red')
                    oval3.draw(window)
                elif self.color == 'green':
                    oval.setOutline('green')
                    oval.draw(window)
                    oval2.setOutline('green')
                    oval2.draw(window)
                    oval3.setOutline('green')
                    oval3.draw(window)
        
    def diamond(self, point):
        """
        Draws the diamond shape on the card, draws either 1, 2 or 3 of them, either green, purple or red, with either solid, stripped or blank fill.
        Parameters:
            self
            point: location of card
        """

        if self.amount == 1:
            poly1 = graphics.Point(point.getX(), point.getY() + 25)
            poly2 = graphics.Point(point.getX() + 15, point.getY())
            poly3 = graphics.Point(point.getX(), point.getY() - 25)
            poly4 = graphics.Point(point.getX() - 15, point.getY())
            poly = graphics.Polygon(poly1, poly2, poly3, poly4)
            
            if self.type == 'solid':
                if self.color == 'purple':
                    poly.setFill('purple')
                    poly.setOutline('purple')
                    poly.draw(window)
                elif self.color == 'red':
                    poly.setFill('red')
                    poly.setOutline('red')
                    poly.draw(window)
                elif self.color == 'green':
                    poly.setFill('green')
                    poly.setOutline('green')
                    poly.draw(window)
                    
            elif self.type == 'stripped':
                if self.color == 'purple':
                    poly.setFill('purple')
                    poly.setOutline('purple')
                    poly.draw(window)
                elif self.color == 'red':
                    poly.setFill('red')
                    poly.setOutline('red')
                    poly.draw(window)
                elif self.color == 'green':
                    poly.setFill('green')
                    poly.setOutline('green')
                    poly.draw(window)
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                for i in range(22): #change the rest of the stripes to 22, 3, 3
                    line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                    line.setOutline('white')
                    line.draw(window)
                    p1y = p1y + 3
                    p2y = p2y + 3
                    
            elif self.type == 'blank':
                if self.color == 'purple':
                    poly.setOutline('purple')
                    poly.draw(window)
                elif self.color == 'red':
                    poly.setOutline('red')
                    poly.draw(window)
                elif self.color == 'green':
                    poly.setOutline('green')
                    poly.draw(window)
                
             
        elif self.amount == 2:
            poly1 = graphics.Point(point.getX() - 30, point.getY() + 25)
            poly2 = graphics.Point(point.getX() - 15, point.getY())
            poly3 = graphics.Point(point.getX() - 30, point.getY() - 25)
            poly4 = graphics.Point(point.getX() - 45, point.getY())
            poly = graphics.Polygon(poly1, poly2, poly3, poly4)
            
            poly1 = graphics.Point(point.getX() + 30, point.getY() + 25)
            poly2 = graphics.Point(point.getX() + 45, point.getY())
            poly3 = graphics.Point(point.getX() + 30, point.getY() - 25)
            poly4 = graphics.Point(point.getX() + 15, point.getY())
            poly2 = graphics.Polygon(poly1, poly2, poly3, poly4)
            
            
            if self.type == 'solid':
                if self.color == 'purple':
                    poly.setFill('purple')
                    poly.setOutline('purple')
                    poly.draw(window)
                    poly2.setFill('purple')
                    poly2.setOutline('purple')
                    poly2.draw(window)
                elif self.color == 'red':
                    poly.setFill('red')
                    poly.setOutline('red')
                    poly.draw(window)
                    poly2.setFill('red')
                    poly2.setOutline('red')
                    poly2.draw(window)
                elif self.color == 'green':
                    poly.setFill('green')
                    poly.setOutline('green')
                    poly.draw(window)
                    poly2.setFill('green')
                    poly2.setOutline('green')
                    poly2.draw(window)
                    
            elif self.type == 'stripped':
                if self.color == 'purple':
                    poly.setFill('purple')
                    poly.setOutline('purple')
                    poly.draw(window)
                    poly2.setFill('purple')
                    poly2.setOutline('purple')
                    poly2.draw(window)
                elif self.color == 'red':
                    poly.setFill('red')
                    poly.setOutline('red')
                    poly.draw(window)
                    poly2.setFill('red')
                    poly2.setOutline('red')
                    poly2.draw(window)
                elif self.color == 'green':
                    poly.setFill('green')
                    poly.setOutline('green')
                    poly.draw(window)
                    poly2.setOutline('green')
                    poly2.setFill('green')
                    poly2.draw(window)
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                for i in range(22):
                    line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                    line.setOutline('white')
                    line.draw(window)
                    p1y = p1y + 3
                    p2y = p2y + 3
             
            elif self.type == 'blank':
                if self.color == 'purple':
                    poly.setOutline('purple')
                    poly.draw(window)
                    poly2.setOutline('purple')
                    poly2.draw(window)
                elif self.color == 'red':
                    poly.setOutline('red')
                    poly.draw(window)
                    poly2.setOutline('red')
                    poly2.draw(window)
                elif self.color == 'green':
                    poly.setOutline('green')
                    poly.draw(window)
                    poly2.setOutline('green')
                    poly2.draw(window)
            
        elif self.amount == 3:
            p1 = graphics.Point(point.getX(), point.getY() + 25)
            p2 = graphics.Point(point.getX() + 15, point.getY())
            p3 = graphics.Point(point.getX(), point.getY() - 25)
            p4 = graphics.Point(point.getX() - 15, point.getY())
            poly = graphics.Polygon(p1, p2, p3, p4)
    
            p1 = graphics.Point(point.getX() + 40, point.getY() + 25)
            p2 = graphics.Point(point.getX() + 55, point.getY())
            p3 = graphics.Point(point.getX() + 40, point.getY() - 25)
            p4 = graphics.Point(point.getX() + 25, point.getY())
            poly2 = graphics.Polygon(p1, p2, p3, p4)
            
            p1 = graphics.Point(point.getX() - 40, point.getY() + 25)
            p2 = graphics.Point(point.getX() - 25, point.getY())
            p3 = graphics.Point(point.getX() - 40, point.getY() - 25)
            p4 = graphics.Point(point.getX() - 55, point.getY())
            poly3 = graphics.Polygon(p1, p2, p3, p4)
            
            if self.type == 'solid':
                if self.color == 'purple':
                    poly.setFill('purple')
                    poly.setOutline('purple')
                    poly.draw(window)
                    poly2.setFill('purple')
                    poly2.setOutline('purple')
                    poly2.draw(window)
                    poly3.setFill('purple')
                    poly3.setOutline('purple')
                    poly3.draw(window)
                elif self.color == 'red':
                    poly.setFill('red')
                    poly.setOutline('red')
                    poly.draw(window)
                    poly2.setFill('red')
                    poly2.setOutline('red')
                    poly2.draw(window)
                    poly3.setFill('red')
                    poly3.setOutline('red')
                    poly3.draw(window)
                elif self.color == 'green':
                    poly.setFill('green')
                    poly.setOutline('green')
                    poly.draw(window)
                    poly2.setFill('green')
                    poly2.setOutline('green')
                    poly2.draw(window)
                    poly3.setFill('green')
                    poly3.setOutline('green')
                    poly3.draw(window)
                    
            elif self.type == 'stripped':
                if self.color == 'purple':
                    poly.setFill('purple')
                    poly.setOutline('purple')
                    poly.draw(window)
                    poly2.setFill('purple')
                    poly2.setOutline('purple')
                    poly2.draw(window)
                    poly3.setFill('purple')
                    poly3.setOutline('purple')
                    poly3.draw(window)
                elif self.color == 'red':
                    poly.setFill('red')
                    poly.setOutline('red')
                    poly.draw(window)
                    poly2.setFill('red')
                    poly2.setOutline('red')
                    poly2.draw(window)
                    poly3.setFill('red')
                    poly3.setOutline('red')
                    poly3.draw(window)
                elif self.color == 'green':
                    poly.setFill('green')
                    poly.setOutline('green')
                    poly.draw(window)
                    poly2.setOutline('green')
                    poly2.setFill('green')
                    poly2.draw(window)
                    poly3.setOutline('green')
                    poly3.setFill('green')
                    poly3.draw(window)
                p1x = point.getX() - 72
                p1y = point.getY() - 34
                p2x = point.getX() + 72
                p2y = point.getY() - 34
                for i in range(22):
                    line = graphics.Line(graphics.Point(p1x, p1y), graphics.Point(p2x, p2y))
                    line.setOutline('white')
                    line.draw(window)
                    p1y = p1y + 3
                    p2y = p2y + 3
                    
            elif self.type == 'blank':
                if self.color == 'purple':
                    poly.setOutline('purple')
                    poly.draw(window)
                    poly2.setOutline('purple')
                    poly2.draw(window)
                    poly3.setOutline('purple')
                    poly3.draw(window)
                elif self.color == 'red':
                    poly.setOutline('red')
                    poly.draw(window)
                    poly2.setOutline('red')
                    poly2.draw(window)
                    poly3.setOutline('red')
                    poly3.draw(window)
                elif self.color == 'green':
                    poly.setOutline('green')
                    poly.draw(window)
                    poly2.setOutline('green')
                    poly2.draw(window)
                    poly3.setOutline('green')
                    poly3.draw(window)
            
                
        
    
    def draw_symbols(self):
        """
        Draws the symbol on the card based on what shape any given card is
        """
        if self.symbol == 'diamond':
            self.diamond(self.point)
        elif self.symbol == 'oval':
            self.oval(self.point)
        elif self.symbol == 'squiggle':
            self.squiggle(self.point)
            
            
    
    def change_attributes(self):
        """
        rerandomizes the attributes of a certain card. This method is used if there is a double of one card in any given grid
        """
        odds_amount = random.randrange(0,3)
        if odds_amount == 0:
            self.amount = 1
        elif odds_amount == 1:
            self.amount = 2
        elif odds_amount == 2:
            self.amount = 3
        
        odds_symbol = random.randrange(0,3)
        if odds_symbol == 0:
            self.symbol = 'diamond'
        elif odds_symbol == 1:
            self.symbol = 'oval'
        elif odds_symbol == 2:
            self.symbol = 'squiggle'
        
        odds_color = random.randrange(0,3)
        if odds_color == 0:
            self.color = 'purple'
        elif odds_color == 1:
            self.color = 'red'
        elif odds_color == 2:
            self.color = 'green'
            
        odds_type = random.randrange(0,3)
        if odds_type == 0:
            self.type = 'solid'
        elif odds_type == 1:
            self.type = 'stripped'
        elif odds_type == 2:
            self.type = 'blank'
        
        
    def highlight(self):
        """
        Highlights any given card object
            Parameters: 
                self
        """
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        for i in range(3):
            point1 = graphics.Point(p1.getX() - i - 1, p1.getY() - i - 1)
            point2 = graphics.Point(p2.getX() + i + 1, p2.getY() + i + 1)
            self.high = graphics.Rectangle(point1, point2)
            self.high.setOutline('blue')
            self.high.draw(window)
    def unhighlight(self):
        """
        Unhighlights any given card
        Parameters:
            self
        """
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        for i in range(3):
            point1 = graphics.Point(p1.getX() - i - 1, p1.getY() - i - 1)
            point2 = graphics.Point(p2.getX() + i + 1, p2.getY() + i + 1)
            self.high = graphics.Rectangle(point1, point2)
            self.high.setOutline('white')
            self.high.draw(window)
    
def get_attributes(totallist):
    """
    Returns the list of attributes of all cards in a given grid """
    attributelist = []
    for cards in totallist:
        atts = cards.getinfo()
        attributelist.append(atts)
    return attributelist
def display_intro():
    """
    Displays the introductory message
    """
    introtxt_header = graphics.Text(graphics.Point(375, 50), 'Welcome to Set')
    introtxt_header.setSize(30)
    introtxt_header.setOutline('blue')
    introtxt_body1 = graphics.Text(graphics.Point(375, 90), 'To play, select any 3 combinations of cards that comprise a set. To win, find all the sets!' )
    introtxt_body2 = graphics.Text(graphics.Point(375, 110), 'A set is when all 3 cards have:'  )
    introtxt_body3 = graphics.Text(graphics.Point(375, 125), '3 charecteristics the same and 1 different')
    introtxt_body4 = graphics.Text(graphics.Point(375, 140), '2 charecteristics the same and 2 different')
    introtxt_body5 = graphics.Text(graphics.Point(375, 155), '1 charecteristics the same and 3 different')
    introtxt_body6 = graphics.Text(graphics.Point(375, 170), 'or 4 different charecteristics')
    introtxt_body7 = graphics.Text(graphics.Point(375, 185), 'The Golden Rule is: if 2 cards have the same charecteristic and the other does not, then it is not a set')
    introtxt_body8 = graphics.Text(graphics.Point(375, 200), 'Click to Begin...')
    introlist = [introtxt_header, introtxt_body1, introtxt_body2, introtxt_body3, introtxt_body4, introtxt_body5, introtxt_body6, introtxt_body7, introtxt_body8]
    for items in introlist:
        items.draw(window)                           
    p = window.getMouse()
    r = window.getMouse()
    for items in introlist:
        items.undraw()
    
    
def getuserchoices(totallist):
    """
    Returns the attributes of a certain card selected by the user
    parameters:
        totallist: a list of card objects 1 - 16
    """
    
    userchoices = []
    highlights = 0
    special_list = []
    cards_list = []
    
    while highlights < 3:
        pt = window.getMouse()
        for cards in totallist:
            if cards.wasClicked(pt):
                info = cards.getinfo()
                if info in special_list:
                    highlights = highlights - 1
                    cards.unhighlight()
                    special_list.remove(info)
                else:
                    cards_list.append(cards)
                    userchoices.append(info)
                    cards.highlight()
                    highlights = highlights + 1
                    special_list.append(info)
    
    for cards in cards_list:
        cards.unhighlight()
    return userchoices
        
def show_sets(totallist):
    """
    finds all the sets in any grid by going through every possible card combination and returns a list of all possible sets with each set being a list of thier own containing thier own attributes
    Parameters:
        totallist: list of all card objects 1-16
    """
    total_sets = 0
    length = len(totallist)
    index1 = 0
    index2 = 0
    index3 = 0
    listofsets = []
    final_list = []
    for i in range(length):
        total_sets = 0
        card1 = totallist[index1].getinfo()
        index1 = index1 + 1
        index2 = 0
        for i in range(length):
            card2 = totallist[index2].getinfo()
            index2 = index2 + 1
            index3 = 0
            for i in range(length):
                card3 = totallist[index3].getinfo()
                index3 = index3 + 1
                variable = is_set(card1, card2, card3)
                possibleset = [card1, card2, card3]
                if variable == 1 and possibleset not in listofsets:
                    possibleset = [card1, card2, card3]
                    possibleset2 = [card1, card3, card2]
                    possibleset3 = [card2, card1, card3]
                    possibleset4 = [card2, card3, card1]
                    possibleset5 = [card3, card2, card1]
                    possibleset6 = [card3, card1, card2]
                    listofsets.append(possibleset)
                    listofsets.append(possibleset2)
                    listofsets.append(possibleset3)
                    listofsets.append(possibleset4)
                    listofsets.append(possibleset5)
                    listofsets.append(possibleset6)
                    final_list.append(possibleset6)
                    
    return final_list
    
def display_how_many():
    """
    Displays how many sets there are, not the actual number, but just the text and the box around it
    """
    name = graphics.Text(graphics.Point(100, 430), 'SETS REMAINING')
    name.setSize(14)
    name.draw(window)
    box = graphics.Rectangle(graphics.Point(25, 417), graphics.Point(175, 460))
    box.setOutline('red')
    box.draw(window)
    
    
    
def finalize_cards(totallist): 
    """
    Ensures that there is only one of each type of card in a grid
    Returns the finalized list of cards 
    Parameters:
        totallist: list of all cards 1 - 16
    """
    attributelist = []
    cardlist = []
    for cards in totallist:
        atts = cards.getinfo()
        if atts in attributelist:
            x = 0
            while x == 0:
                cards.change_attributes()
                new_atts = cards.getinfo()
                if new_atts in attributelist:
                    x = 0
                else: #new_atts not in attributelist:
                    attributelist.append(atts)
                    cardlist.append(cards)
                    x = 1
        elif atts not in attributelist:
            attributelist.append(atts)
            cardlist.append(cards)
    return cardlist
    
def draw_all(cardlist):
    """
    draws all cards in cardlist
    Parameters:
        cardlist: finalized list of cards in a grid
    """
    for cards in cardlist:
        cards.draw_symbols()
    
def is_set(choice1, choice2, choice3):
    """
    Determines if a combination is a set (3 same, 1 different), (2 same, 2 different), (3 different 1 same, or all different) 
    Returns 1 if it is a set and 0 if it is not
    Parameters:
        choice1, choice2, choice3: 3 selections of cards
    """
    tallysame = 0 
    tallydiff = 0
    for i in range(4): 
        if choice1[i] == choice2[i] and choice1[i] == choice3[i]:
            tallysame = tallysame + 1
    
    for i in range(4):  
        if choice1[i] != choice2[i] and choice1[i] != choice3[i] and choice2[i] != choice3[i]:
            tallydiff = tallydiff + 1

    if tallysame == 3 and tallydiff == 1:
        return 1
    elif tallysame == 2 and tallydiff == 2:
        return 1
    elif tallydiff == 3 and tallysame == 1:
        return 1
    elif tallydiff == 4:
        return 1
    else:
        return 0
        
def play_game(total, setslist, count, totallist):
    """
    Plays the actual game: gets users choices and determines if they are a set, if they are a set, prints out that it is a set and adds that set (and all possible combinations of that set) to a list so the same set cannot be selected again in a differnt order
    Returns count: the number of sets still left in the grid
    Parameters:
        total: text object that displays how many sets are left in the grid
        setslist: list of sets already found by the user
        count: number of sets on the grid
        card objects 1 - 16
    """
            
    choice = getuserchoices(totallist)
    
    choice1 = choice[0]
    choice2 = choice[1]
    choice3 = choice[2]
    
    possible_set = [choice1, choice2, choice3]
    possible_set2 = [choice1, choice3, choice2]
    possible_set3 = [choice2, choice1, choice3]
    possible_set4 = [choice2, choice3, choice1]
    possible_set5 = [choice3, choice2, choice1]
    possible_set6 = [choice3, choice1, choice2]
    
    #print('-------------')
    #print(choice1)
    #print(choice2)
    #print(choice3)             #Uncomment to see terminal interface
    #print('-------------')
    
    if possible_set in setslist:
        #print('You have already found this set')
        return 3
            
    elif is_set(choice1, choice2, choice3) == 1:
        #print('Found Set!')
        setslist.append(possible_set)
        setslist.append(possible_set2)
        setslist.append(possible_set3)
        setslist.append(possible_set4)
        setslist.append(possible_set5)
        setslist.append(possible_set6)
        return 1
    else:
        #print('Not a set')
        return 0

def run_interface(lists_of_sets, count, setslist, totallist):
    """
    Runs the interface on the window and calculates when the user has found all the sets
    
    Parameters:
        list_of_sets: list of sets in the grid, uncomment to see the sets
        count: how many sets there are in the grid
        sets_list: list of found sets and all possible comination of a set
        totallist: list of card objects 1-16
        
    Return value: none
    """
    foundset = graphics.Text(graphics.Point(362, 201), 'Found SET!')
    foundset.setSize(20)
    foundset.setOutline('blue')
    foundtxt = graphics.Text(graphics.Point(362, 435), 'You have already found this set')
    foundtxt.setSize(13)
    victorytxt = graphics.Text(graphics.Point(361, 199), 'Found all the Sets!')
    victorytxt.setSize(35)
    victorytxt.setOutline('blue')
    click_to_cont = graphics.Text(graphics.Point(362, 450), '(click to continue)')
    click_to_cont.setSize(13)
    display_how_many()
    total = graphics.Text(graphics.Point(100, 450), count)
    total.setSize(20)
    total.draw(window)
    not_a_set = graphics.Text(graphics.Point(362, 435), 'Not a set')
    not_a_set.setSize(13)
    previous_count = count
    
    for items in lists_of_sets:  #Uncomment to display the sets in a grid
            print(items)
    
    while count > 0: 
        if previous_count != count:
            total.undraw()
            total = graphics.Text(graphics.Point(100, 450), count)
            total.setSize(20)
            total.draw(window)
            foundset.draw(window)
            click_to_cont.draw(window)
            m = window.getMouse()
            click_to_cont.undraw()
            foundset.undraw()
            previous_count = count
        was_set = play_game(total, setslist, count, totallist)
        if was_set == 1:
            count = count - 1 
        if was_set == 3:
            drawn = 1
            foundtxt.draw(window)
            click_to_cont.draw(window)
            t = window.getMouse()
            click_to_cont.undraw()
            foundtxt.undraw()
        if was_set == 0:
            not_a_set.draw(window)
            click_to_cont.draw(window)
            t = window.getMouse()
            click_to_cont.undraw()
            not_a_set.undraw()
    total.undraw()
    count = 0
    total = graphics.Text(graphics.Point(100, 450), count)
    total.setSize(20)
    total.draw(window)
    victorytxt.draw(window)
    m = window.getMouse()
    window.close()
    print('Found all the Sets!')
    
def initalize_cards():
    """
    Creates 16 card objects all with unique attributes
    Parameters: non
    Returns totallist: list of all card objects
    """
    var = 0
    while var == 0:
        c1 = card(graphics.Point(100,50), 150, 75)
        c2 = card(graphics.Point(275,50), 150, 75)
        c3 = card(graphics.Point(450,50), 150, 75)
        c4 = card(graphics.Point(625,50), 150, 75)
        c5 = card(graphics.Point(100,150), 150, 75)
        c6 = card(graphics.Point(275,150), 150, 75)
        c7 = card(graphics.Point(450,150), 150, 75)
        c8 = card(graphics.Point(625,150), 150, 75)
        c9 = card(graphics.Point(100, 250), 150, 75)
        c10 = card(graphics.Point(275, 250), 150, 75)
        c11 = card(graphics.Point(450, 250), 150, 75)
        c12 = card(graphics.Point(625,250), 150, 75)
        c13 = card(graphics.Point(100, 350), 150, 75)
        c14 = card(graphics.Point(275, 350), 150, 75)
        c15 = card(graphics.Point(450, 350), 150, 75)
        c16 = card(graphics.Point(625, 350), 150, 75)
        
        totallist = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]
        
        cardlist = finalize_cards(totallist)
        lists_of_sets = show_sets(totallist)
        count = len(lists_of_sets)
        
        if count < 3: #minimum amount of sets you want to find
            print('not enough sets, reshuffling')
        else:
            var = 1
            draw_all(cardlist)
            
    return totallist

def main():
    display_intro()
    totallist = initalize_cards()
    setslist = []
    lists_of_sets = show_sets(totallist)
    count = len(lists_of_sets)
    run_interface(lists_of_sets, count, setslist, totallist)
    

if __name__ == '__main__':
    main()

        
                
        