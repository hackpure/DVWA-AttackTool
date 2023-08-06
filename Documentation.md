# DVWA-AttackTool
DVWA CyberSecurity Internal Practice Environmnent Tool
# [Developed By - hacpure]
  Contact At - https://github.com/hackpure


Greetings to the users of DVWA Brute-Force

This tool is explicitly designed to test DVWA against the BruteForce vulnerability attacking the Web-Application
with usernames and passwords that are most common and are vulnerable using the CLUSTER BOMB Approach.

THE CLUSTER BOMB APPROACH :-

		The Cluster Bomb Approach [Payload Sets : 2]
			
			Payload Set 1
			
			Payload Set 2
			
		Cluster Bomb Approach uses the technique of trying every possible combination of Payload Set 1 with Payload Set 2

		The total number of requests/hits done are the product of total number of values in Payload Set 1 to number of values 
		in Payload Set 2
		
			{ Example : 
					Payload Set 1 : 7 [Usernames]
					Payload Set 2 : 10 [Passwords]
					Total Requests : 7 x 10 = 70 [Requests]
			}

BEHIND THE SCENES OF CLUSTER BOMB APPROACH :-

		BEHIND THE SCENES OF CLUSTER BOMB OF APPROACH

			Payload Set 1 : 7 [Usernames]
			Payload Set 2 : 3 [Passwords]
			
			
			Attack/Hit 1 :-
			
				{ Payload Set 1 : Value 1, Payload Set 2 : Value 1 }
			
			Attack/Hit 2 :-
	
				{ Payload Set 1 : Value 1, Payload Set 2 : Value 2 }

			Attack/Hit 3 :-
		
				{ Payload Set 1 : Value 1, Payload Set 2 : Value 3 }

			Attack/Hit 4 :- 
	
				{ Payload Set 1 : Value 2, Payload Set 2 : Value 1 }

			Attack/Hit 5 :-
	
				{ Payload Set 1 : Value 2, Payload Set 2 : Value 2 }

			Attack/Hit 6 :-

				{Payload Set 1 : Value 2, Payload Set 2 : Value 3 }

									and so on ...				


Usage :-

	python3 brute-force.py


Requirements and Environment Setup :-
	
	pip3 install -r requirements.txt
	python3 setup.py


#Note : This Script Is Currently Tested On Low Level Of Security May Cause Some ErrorIn Other Levels

####### $[ Update ] : In Future Updates This Maybe A Full Testing Tool For DVWA.
