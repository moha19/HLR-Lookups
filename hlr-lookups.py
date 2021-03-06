#!/usr/bin/env python

import sys
import requests
import re
import json
import os
import getpass
import time

'''This script is used to automate hlr-lookup process and extract important data from it
	it uses the http api proivded by hlr-lookups application (curl), this script works for Qtel, Zain KW, Etisalat UAE,DU UAE, jawal palestine'''


def hlrLookup(argv,username,passwd):
		try:
			#Zain Kuwait
			if argv[1:5] == '9659':
				response_msc = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=NT7&storage=CURL-TEST&username="+username+"&password="+passwd)
				response_imsi = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
				
				mccmnc = response_imsi.json()['results'][0]['mccmnc']
				
				if type(response_imsi.json()['results'][0]['msin']) != None:
					msin = response_imsi.json()['results'][0]['msin']
					imsi_ver = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
					msin_ver = imsi_ver.json()['results'][0]['msin']
					print "\033[34m[*]\033[0mChecking for Home Routing/SMS FW..."

					#Checking for home routing/sms FW
					if msin == msin_ver:
						print "\033[32m[+]\033[0mTarget IMSI: " + mccmnc + msin
					else:
						print "\033[93m[!]\033[0mPossible Implementation of Home Routing Detected: IMSI is Scrambled {"+mccmnc + msin+", "+mccmnc + msin_ver+"}"

				else:
					print "\033[32m[-]\033[0mTarget IMSI is Null"

				if type(response_imsi.json()['results'][0]['msin']) != None:
					msc = response_msc.json()['results'][0]['servingmsc']
					msc_2 = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=NT7&storage=CURL-TEST&username="+username+"&password="+passwd)
					msc_ver = msc_2.json()['results'][0]['servingmsc']

					if msc == msc_ver:
						print "\033[32m[+]\033[0mTarget Serving MSC: "+ msc
					else:
						print "\033[93m[!]\033[0mDifferent MSC GT returned: Further Scanning Required {"+msc+", "+msc_ver+"}"

				if type(response_imsi.json()['results'][0]['msin']) != None:
					hlr = response_imsi.json()['results'][0]['servinghlr']
					print "\033[32m[+]\033[0mTarget's HLR: " + hlr

				network_name = response_imsi.json()['results'][0]['originalnetworkname']
				print "\033[32m[+]\033[0mTarget's Operator: " + network_name

	
				

				print "\033[34m[*]\033[0mInformation Retrieved at " + time.asctime()
			###################################################################################
			#Etisalat UAE
			elif argv[1:6] == '97150' or argv[1:6] == '97154' or argv[1:6] == '97156':
				response_msc = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=NT7&storage=CURL-TEST&username="+username+"&password="+passwd)
				response_imsi = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
				
				
				mccmnc = response_imsi.json()['results'][0]['mccmnc']
				
				if type(response_imsi.json()['results'][0]['msin']) != None:
					msin = response_imsi.json()['results'][0]['msin']
					imsi_ver = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
					msin_ver = imsi_ver.json()['results'][0]['msin']
					print "\033[34m[*]\033[0mChecking for Home Routing/SMS FW..."

					#Checking for home routing/sms FW
					if msin == msin_ver:
						print "\033[32m[+]\033[0mTarget IMSI: " + mccmnc + msin
					else:
						print "\033[93m[!]\033[0mPossible Implementation of Home Routing Detected: IMSI is Scrambled {"+mccmnc + msin+", "+mccmnc + msin_ver+"}"


				else:
					print "\033[32m[-]\033[0mTarget IMSI is Null"

				
				if type(response_imsi.json()['results'][0]['msin']) != None:
					msc = response_msc.json()['results'][0]['servingmsc']
					msc_2 = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=NT7&storage=CURL-TEST&username="+username+"&password="+passwd)
					msc_ver = msc_2.json()['results'][0]['servingmsc']

					if msc == msc_ver:
						print "\033[32m[+]\033[0mTarget Serving MSC: "+ msc
					else:
						print "\033[93m[!]\033[0mDifferent MSC GT returned: Further Scanning Required {"+msc+", "+msc_ver+"}"


				if type(response_imsi.json()['results'][0]['msin']) != None:
					hlr = response_imsi.json()['results'][0]['servinghlr']
					print "\033[32m[+]\033[0mTarget's HLR: " + hlr

				network_name = response_imsi.json()['results'][0]['originalnetworkname']
				print "\033[32m[+]\033[0mTarget's Operator: " + network_name
		
				print "\033[34m[*]\033[0mInformation Retrieved at " + time.asctime() 
			###################################################################################
			#DU UAE
			elif argv[1:6] == '97155' or argv[1:6] == '97152':
				response_msc = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=NT7&storage=CURL-TEST&username="+username+"&password="+passwd)
				response_imsi = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
				
				
				
				mccmnc = response_imsi.json()['results'][0]['mccmnc']
				
				if type(response_imsi.json()['results'][0]['msin']) != None:
					msin = response_imsi.json()['results'][0]['msin']
					imsi_ver = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
					msin_ver = imsi_ver.json()['results'][0]['msin']
					print "\033[34m[*]\033[0mChecking for Home Routing/SMS FW..."

					#Checking for home routing/sms FW
					if msin == msin_ver:
						print "\033[32m[+]\033[0mTarget IMSI: " + mccmnc + msin
					else:
						print "\033[93m[!]\033[0mPossible Implementation of Home Routing Detected: IMSI is Scrambled {"+mccmnc + msin+", "+mccmnc + msin_ver+"}"

				else:
					print "\033[32m[-]\033[0mTarget IMSI is Null"

				if type(response_imsi.json()['results'][0]['msin']) != None:
					msc = response_msc.json()['results'][0]['servingmsc']
					msc_2 = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=NT7&storage=CURL-TEST&username="+username+"&password="+passwd)
					msc_ver = msc_2.json()['results'][0]['servingmsc']

					if msc == msc_ver:
						print "\033[32m[+]\033[0mTarget Serving MSC: "+ msc
					else:
						print "\033[93m[!]\033[0mDifferent MSC GT returned: Further Scanning Required {"+msc+", "+msc_ver+"}"

				if type(response_imsi.json()['results'][0]['msin']) != None:
					hlr = response_imsi.json()['results'][0]['servinghlr']
					print "\033[32m[+]\033[0mTarget's HLR: " + hlr

				network_name = response_imsi.json()['results'][0]['originalnetworkname']
				print "\033[32m[+]\033[0mTarget's Operator: " + network_name
		
				print "\033[34m[*]\033[0mInformation Retrieved at " + time.asctime() 

			###################################################################################
			#QTEL
			elif argv[1:5] == '9743' or argv[1:5] == '9744' or argv[1:5] == '9745' or argv[1:5] == '9746':
				response_msc = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=SV3&storage=CURL-TEST&username="+username+"&password="+passwd)
				response_imsi = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
								
				mccmnc = response_imsi.json()['results'][0]['mccmnc']
				
				if type(response_imsi.json()['results'][0]['msin']) != None:
					msin = response_imsi.json()['results'][0]['msin']
					imsi_ver = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
					msin_ver = imsi_ver.json()['results'][0]['msin']
					print "\033[34m[*]\033[0mChecking for Home Routing/SMS FW..."

					#Checking for home routing/sms FW
					if msin == msin_ver:
						print "\033[32m[+]\033[0mTarget IMSI: " + mccmnc + msin
					else:
						print "\033[93m[!]\033[0mPossible Implementation of Home Routing Detected: IMSI is Scrambled {"+mccmnc + msin+", "+mccmnc + msin_ver+"}"

				else:
					print "\033[32m[-]\033[0mTarget IMSI is Null"

				if type(response_imsi.json()['results'][0]['msin']) != None:
					msc = response_msc.json()['results'][0]['servingmsc']
					msc_2 = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=SV3&storage=CURL-TEST&username="+username+"&password="+passwd)
					msc_ver = msc_2.json()['results'][0]['servingmsc']

					if msc == msc_ver:
						print "\033[32m[+]\033[0mTarget Serving MSC: "+ msc
					else:
						print "\033[93m[!]\033[0mDifferent MSC GT returned: Further Scanning Required {"+msc+", "+msc_ver+"}"

				if type(response_imsi.json()['results'][0]['msin']) != None:
					hlr = response_imsi.json()['results'][0]['servinghlr']
					print "\033[32m[+]\033[0mTarget's HLR: " + hlr

				network_name = response_imsi.json()['results'][0]['originalnetworkname']
				print "\033[32m[+]\033[0mTarget's Operator: " + network_name


				print "\033[34m[*]\033[0mInformation Retrieved at " + time.asctime()
			###################################################################################
			#Jawal Palestine
			elif argv[1:6] == '97259':
				response_msc = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=SV3&storage=CURL-TEST&username="+username+"&password="+passwd)
				response_imsi = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
				
				mccmnc = response_imsi.json()['results'][0]['mccmnc']
				
				if type(response_imsi.json()['results'][0]['msin']) != None:
					msin = response_imsi.json()['results'][0]['msin']
					imsi_ver = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=IP1&storage=CURL-TEST&username="+username+"&password="+passwd)
					msin_ver = imsi_ver.json()['results'][0]['msin']
					print "\033[34m[*]\033[0mChecking for Home Routing/SMS FW..."

					#Checking for home routing/sms FW
					if msin == msin_ver:
						print "\033[32m[+]\033[0mTarget IMSI: " + mccmnc + msin
					else:
						print "\033[93m[!]\033[0mPossible Implementation of Home Routing Detected: IMSI is Scrambled {"+mccmnc + msin+", "+mccmnc + msin_ver+"}"

				else:
					print "\033[32m[-]\033[0mTarget IMSI is Null"

				if type(response_imsi.json()['results'][0]['msin']) != None:
					msc = response_msc.json()['results'][0]['servingmsc']
					msc_2 = requests.get("https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest&msisdn="+argv+"&route=SV3&storage=CURL-TEST&username="+username+"&password="+passwd)
					msc_ver = msc_2.json()['results'][0]['servingmsc']

					if msc == msc_ver:
						print "\033[32m[+]\033[0mTarget Serving MSC: "+ msc
					else:
						print "\033[93m[!]\033[0mDifferent MSC GT returned: Further Scanning Required {"+msc+", "+msc_ver+"}"

				if type(response_imsi.json()['results'][0]['msin']) != None:
					hlr = response_imsi.json()['results'][0]['servinghlr']
					print "\033[32m[+]\033[0mTarget's HLR: " + hlr

				network_name = response_imsi.json()['results'][0]['originalnetworkname']
				print "\033[32m[+]\033[0mTarget's Operator: " + network_name


				print "\033[34m[*]\033[0mInformation Retrieved at " + time.asctime()
			###################################################################################

		except :
			if response_imsi.json()['success'] is False:
				print '\033[31m[-]Error:\033[0m ', response_imsi.json()['errors']
			elif response_msc.json()['success'] is False:
				print '\033[31m[-]Error:\033[0m ',response_imsi.json()['errors']
			sys.exit(1)
		
	
	


if __name__=='__main__':

	if len(sys.argv) < 2:

		print "\n\033[93mUsage:\033[0m ./hlr-lookup.py <MSISDN>"
		print "\033[93mExample:\033[0m ./hlr-lookup.py +20123456789"
		sys.exit(1)

	elif  (len(sys.argv[1][1:]) != 11) and (len(sys.argv[1][1:]) != 12):
		print "\033[91m[-]\033[0mWrong Format for MSISDN"
		print "\033[34m[*]\033[0mMSISDN should be 11 or 12 digits after the (+) sign"
		sys.exit(1)

	else:
		username = raw_input("\033[34m[*]\033[0mEnter your username: ")
		passwd = getpass.getpass("\033[34m[*]\033[0mEnter your API password: ")
		print "\033[34m[*]\033[0mSending Request..."
		hlrLookup(sys.argv[1], username, passwd)
		
