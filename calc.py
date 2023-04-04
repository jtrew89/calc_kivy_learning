##if the design aspect of the app is in a design kivy file, you do not need to import design modules

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#set the app window size
Window.size = (400,600)

#builder allows you to use specific design files for specic portions of the app, so that you can use more than 1
Builder.load_file('calc.kv')

##make grid for app
class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'
	#Button pressing function
	def button_press(self, button):
		#variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text

		#determine if 0 i in place
		if prior == "0":
			self.ids.calc_input.text = ''
			self.ids.calc_input.text = f'{button}'

		else:
			self.ids.calc_input.text = f'{prior}{button}'

	#create addition function
	def add(self):
		
		#variable of value already in unput text box
		prior = self.ids.calc_input.text
		
		#include + sign to text box
		self.ids.calc_input.text = f'{prior}+'

	#create subtraction function
	def subtract(self):
		
		#variable of value already in unput text box
		prior = self.ids.calc_input.text
		
		#include + sign to text box
		self.ids.calc_input.text = f'{prior}-'

	#create division function
	def divide(self):
		
		#variable of value already in unput text box
		prior = self.ids.calc_input.text
		
		#include + sign to text box
		self.ids.calc_input.text = f'{prior}/'

	#create addition function
	def multiply(self):
		
		#variable of value already in unput text box
		prior = self.ids.calc_input.text
		
		#include + sign to text box
		self.ids.calc_input.text = f'{prior}*'

	#create equals function
	def equals(self):
		prior = self.ids.calc_input.text

		#Addition
		if '+' in prior:
			num_list = prior.split('+')
			answer = 0 

			#loop through list
			for num in num_list:
				answer = answer + int(num)

			#print answer in the text box
			self.ids.calc_input.text = str(answer)


class CalculatorApp(App): #whatever the build class is called, the supporting kivy design file must be named similarly (without capital letters), e.g. my.kv. This file has to be in the same directory, that is why there is no reference to it
    
    def build(self):
        return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()