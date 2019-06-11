def exception(e):pass
helpl=''
karts=[]
import traceback,requests
from bs4 import *
pre=lambda x,y:x
rn=lambda x:x
alink=lambda x,y:x
from threading import Thread
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120"}
from config import *
out=open('z','a')
class Thread2(Thread):
	def __init__(self, target=None,args=(), kwargs={}):
		Thread.__init__(self,None, target, None, args, kwargs)
		self._return = None

	def run(self):
		try:
			if self._target:
				self._return = self._target(*self._args, **self._kwargs)
		finally:
			del self._target, self._args, self._kwargs

	def join(self):
		Thread.join(self)
		return self._return

deb=['14CSL260','14MER137','14EEL133','14CSR098','14ITR021','14ISR029','14CER043','14CER075','14CER192','15CEL267','15MER102','15MER156','13ECR008','14ECR022','15ECR037','15EIL109','14CSR203','15CSR068','15CSL260','15CHL122','15BCR049','14BSR009','15ISR045','16CER076','16CEL257','16MER062','16AUR055','16EER049','16EEL138','16EIR017','16ITR035','16ITR053','16CMR007','16ESR002','16CIR009','16BIR012','16MCL018','16MCL055','17CER021','17CER104','17MER020','17MER030','17AUR051','17CSR026','17BSR058','17BSR059','17CMR002','17MMR001','17VLR002','17MBR008','17MBR037','17MBR102','17ISR026']
deb2={
	'15CSR068':1,'14CSL260':0
}
deb3={
	'14CSL260':2
}

cse_b=list(range(61,120+1))+list(range(248,252+1))+['14CSL260']
def dell(*i):
	for i in i:
		del cse_b[cse_b.index(i)]
dell(68,82,114)	
cse=range(1,260+1)


def req(j):
	for i in range(5):
			try:
				# print(j)
				# s=requests.Session()
				# s.headers.update(headers)
				r =  requests.get(j)
				if 0 and j[1]:
					cpt=scr.kec(s,proxies)
					r= s.post(j[0],data={'captcha':cpt,'submit':'Submit'})
				## OMG; they set response to 500 ; 
				if not r or r.text=='<html>\n</html>\n':
					# print(i,r,r.url,r.text)
					# continue
					# raise  Exception('PX')
					pass
			except Exception as e:
				print('#',e)
				# traceback.print_exc()
				# proxy()
				# if not i:exception(e)
				sleep(20)
			else:break
	else:return 'E'
	return r

def dipres(rn):
  try:
    f=requests.get(f"http://112.133.214.75/result_Apr2019/display.php?regno={rn}&scheme=k", headers=headers)
    r=(BeautifulSoup(f.text,"lxml"))
    j=0
    tab1=r.select('table')[0].select('tr')
    x=("Name   : "+tab1[0].select('td')[1].text.strip()+"\nReg No : "+tab1[1].select('td')[1].text+"\nDept   : "+tab1[2].select('td')[1].text)
    for i in range(1,9):
      j+=int(r.select('table')[1].select('tr')[i].select('td')[3].text)
    x+=(f"\nResult : {r.select('table')[1].select('tr')[10].select('td')[1].text}\nTotal  : {j} \nAverage : {j/8}%\n{alink(f'http://mechsteed.pythonanywhere.com/dip/{rn}','More')}\n@MassDhiva-@Abishakkumar ")
    return x
  except Exception as e:
    return str(e)

def cgf(rn,pres=1):
	if rn=='h':
		return '''
		cg.rn 	->	cgpa for cseb
		'''
	return pre(requests.get(f'http://smartmanoj.pythonanywhere.com/cgf/{rn}').text.replace('<br>',''),pres)
def cgf2(rn):
	if rn=='h':
		return '''
		cv.rn 	->	cgpa for cseb - XL Friendly
		'''
	try:
		a=[i.split(', ')[-1] for i in cgf(rn,0).replace('0.00','NIL').splitlines()[2:]]
		if 'NIL' not in a:a.extend(['NIL']*3)
		return '\t'.join(a)
	except Exception as e:
		return str(e)
def cnc(s):return ''.join(i[0] for i in s.split() if i[0].isupper())	
def strn(s):return ', '.join([f'{i:.2f}'for i in s])
def cg(sn=None,rn=None,dob='00.00.0000',verbose=1,pres=1,get_name=0):
	if rn in helpl:
		return '''
		cg.rn.dob 		cgpa
		cg@sem.rn.dob	sem ( 0 for last)
		cg@SPL.rn.dob	rv,ar,sp
		cg@^.rn 		RA to E
		http://j.mp/markanalyze
		rv  - Revaluation 
		ar  - Arrear
		sp  - Supplementary 
		'''
	
	if rn=='fgs':return fgs
	else:rn=rn.upper()
	# print('@',rn,dob)
	cp={'S':10,'A':9,'B':8,'C':7,'D':6,'E':5,'RA':0,'WH':0,'W':0,'AB':0}
	cp2 = {v: k for k, v in cp.items()}
	if sn and sn[-1]=='^':
		cp['RA'] = 5
		sn=sn.rstrip('^')
	wiki=[]
	wiki2={}
	try:
		yr=int(rn[:2])
		tty=(yr-15)*2 +(deb2.get(rn, rn in deb))
		fst='http://results.kongu.edu/allresout.php?regno='
		allres=7
		new=1-(deb3.get(rn, 0)) 
		tth=allres-tty
		tt=tth+new #if new
		for i in range(tth):
			ooe=['ODD','EVEN'][i%2]
			wiki.append((fst+rn+"-{}_{}".format(ooe,yr+2000+(i+1)//2-i%2)))
		# print(wiki)
			# wiki.append((fst+rn+"-{0}_{3}-{1}_{2}".format(ooe,mnt,yr+2000+(i+1)//2,yr+2000+(i+1)//2-i%2),0))

		if tt==1: #first yr
			wiki.append(("http://results.kongu.edu/ovio.php?regno="+rn))
			# wiki2['ar']=("http://results.kongu.edu/oodxviir.php?regno={}&dob={}".format(rn,dob))
			# wiki2['sp']=("http://results.kongu.edu/tkviiospo.php?regno={}&dob={}".format(rn,dob))
			# wiki2['rv']=("http://results.kongu.edu/xxviioiso.php?regno={}".format(rn))
			pass


		else:
			wiki.append("http://results.kongu.edu/eofrego.php?regno="+rn)
			wiki2['pre']=(("http://results.kongu.edu/efregpao.php?regno="+rn))
			# wiki2['ar']=("http://results.kongu.edu/aoviiiaro.php?regno={}".format(rn,dob))
			# wiki2['sp']=("http://results.kongu.edu/tkviiospo.php?regno={}&dob={}".format(rn,dob))
			# wiki2['rv']=("http://results.kongu.edu/tkviiorvo.php?regno={}&dob={}".format(rn,dob))
			pass
		mar=""
		n=10
		cgpa=[0]*n
		zcgpa=[0]*n
		ztcgpa=[0]*n
		gpa=[0]*n
		zgpa=[0]*n
		data = [{} for x in range(n)]
		cd=[{} for x in range(n)]
		if '14'== rn[:2]  and '14ISR'!= rn[:5]  and not sn and rn not in deb:sn=10
		if sn :

			if sn==10:g="http://results.kongu.edu/evxviifyo.php?regno={}&dob={}".format(rn,dob),1;sn=8
			else:
				try:
					if sn.isdigit():
						sn=int(sn)
						g=wiki[sn-1]
					else:
						g=wiki2.get(sn)
						if not g:raise Exception
				except Exception as e:
					return 'Not Yet'
			r=req(g)
			if r=='E':return 'Error R'
			if 'Invalid' in r.text:return 'Invalid Data'
			s = BeautifulSoup(r.text,"lxml")
			id=s.find_all('font')
			print(s)
			name=id[3].string
			roll=id[4].string	
			if get_name:return name,roll		
			table = s.find_all('table',attrs={"rules":"ALL"})
			rt='{}\n{}\nSem :{}'.format(name,roll,sn)
			rows = table[0].find_all('tr')
			x=y=0
			for row in rows[1:]:
				cols = row.find_all('td')+row.find_all('th')
				cols = ([int(x)  if x.isdigit() else x for x in [ele.text.strip() for ele in cols ] ])
				f=f'{cnc(cols[2]):5}'
				cols[3]=float(cols[3])
				if cols[0]!=sn:f+=f'{(cols[0])}'
				else:x+=cols[3];
				y+=cols[3]*cp[cols[4]]
				rt+=('\n{:8} - {}'.format(f,cols[4]))

			qcgpa=''
			qgpa=''
			if(isinstance(sn,str) or sn>=tth):
				gpaf=s.find_all("font",style="/font/Scan me")
				if(len(gpaf)):
					qgpa='GPA  :'+gpaf[0].text
					
			else:
				gpaf=s.find_all("font")
				if(len(gpaf)):
					qgpa='GPA  :'+gpaf[8].text
					qcgpa='CGPA :'+gpaf[12].text
			tre= '{}\n{}\n{}'.format(rt,qgpa,qcgpa).strip()
			if sn==8:tre+=f'\n{"CREDITS":<8} - {y/10}/{x}'
		else:
			t=[]
			for i,j in enumerate((wiki+list(wiki2.values()))):
				if(('R'!= rn[4] ) and i<2):
					t.append(None)
					continue
				z=Thread2(target=req, args=(j,))
				z.start()
				t.append(z)
			res=[t.join() if t else t for t in t]
			for i,r in enumerate(res):
				#bug
				if not r and i!=len(res)-1:continue
				if r=='E':return 'Error R'
				if 'Register Number Invalid..' in r.text  :
					if j in wiki2.values() : continue
					return 'Invalid Data'
				s = BeautifulSoup(r.text,"lxml")
				font=s.select('font')
				if len(font)<3:
					print(ascii(r.text))
				name=font[3]
				roll=font[4]			
				table = s.find_all('table',attrs={"rules":"ALL"})
				rows = table[0].find_all('tr')
				for row in rows[1:]:
					cols = row.find_all('td')+row.find_all('th')
					cols = ([int(x)  if x.isdigit() else x for x in [ele.text.strip() for ele in cols ] ])
					cols[3]=float(cols[3])
					cd[cols[0]-1][cols[2]]=cols[3]
					cols[3]=cols[3]*cp[cols[4]]
					data[cols[0]-1][cols[2]]=cols[3]

				if(i>=tth):
					gpaf=s.find_all("font",style="/font/Scan me")
					if(len(gpaf)):
						gpa[i]=gpaf[0].text
						
				else:	
					gpaf=s.find_all("font")
					if(len(gpaf)):
						gpa[i]=gpaf[8].text
						cgpa[i]=gpaf[12].text
				if gpa[i]=="---":
					gpa[i]="0"
				if cgpa[i]=="---":
					cgpa[i]="0"

			z1=z2=z3=z4=0
			zxc=0
			zxd=1
			dbg=''
			for i in range(tt):
				if(('L' in rn) and i<2) :continue
				x,y=sum(data[i].values()),sum(cd[i].values())
				z1+=x
				z2+=y
				if(0 in data[i].values()):
					gpa[i]=0
					zxc=1
					if i>1:zxd=0
					continue
				
				if y:zgpa[i]=round(x/y+1e-15,2) 
				ygpa=float(str(gpa[i]).strip('*'))
				if(ygpa and zgpa[i]!=ygpa):
					dbg+=(str(('#g ',rn,i+1,zgpa[i],gpa[i])))

				if i >1 and zxd:z3+=x;z4+=y;ztcgpa[i]=round(z3/z4+1e-15,2) 

				if zxc:
					cgpa[i]=0
					continue
				zcgpa[i]=round(z1/z2+1e-15,2) 
				if(i==tth):cgpa[i]=zcgpa[i]
				ycgpa=float(cgpa[i])
				if(ycgpa and zcgpa[i]!=ycgpa):
					dbg+=(str(('#cg',rn,i+1,zcgpa[i],cgpa[i])))
			if 0:
				print('---')
				for i in range(7):
					print(i+1)
					for s,t in data[i].items():
						g=cd[i][s]
						print('{:50} {} ({})'.format(s,cp2[t//g],g))
					print('GPA  :',zgpa[i])
					print('CGPA :',zcgpa[i])
					print('-'*50)
			acount=0
			alist={}
			for x in range(tt):
				alist[x]=[]
				for y in data[x]:
					if data[x][y]==0:
						acount+=1
						alist[x].append(y)
			x=7
			tre=f'{name.string}\n{roll.string}\n{"GPA": <{x}}: {strn(zgpa[:tt])}\n{"CGPA": <{x}}: {strn(zcgpa[:tt])}'
			tre2=f'{roll.string},{name.string},{strn(zcgpa[:tt])}'
			print(tre2,file=out)
			if rn[2:4] not in karts+['MS'+'IF']:
				tre+=f'\n{"TCGPA": <{x}}: {strn(ztcgpa[:tt])}'
			if (all(cd[:7])):
				tre+=f'\n{"CREDITS":<{x}}: {z1/10}/{z2}'
			if acount and verbose:
				tre+=('\nNo. of arrears:{}\n'.format(acount))
				for z in alist:
					if alist[z]:tre+=('{{{}-{}}}\n'.format(z+1,alist[z]))
			if dbg and rn not in ['14CSL260']:
				tre+=dbg
	except  Exception as e:
		tre=str(e)
		print('#',traceback.print_exc())
	return pre(tre,pres) +(alink(r.url,'More') if sn else '')

a='15CSR158,15CSR226'.split(',')
if __name__ == '__main__':
	# proxies={}
	# print(cg(rn='17MSR006'))
	# z=cg(rn=rn('77'));print(z)
	# z=cg(rn=rn('94'));print(z)
	# z=dipres('19303689');print(z);exit()
	# z=cg(sn='',rn=('18msr007'));print(z)
	z=cg(rn=rn('18msr001'),sn='');print(z);exit()
	for i in a:
		z=cg(rn=i,sn='',pres=0);print(z)
	if 0:
		z=cg(rn='18CER003',sn='');print(z)
		z=cg(rn='18CER003',sn='');print(z)
		z=cg(rn='16CER023',sn='1');print(z)
	if 0:
		for i in range(1,121):
			try:
				# if i>102:
					z=cg(rn=f"18mbr{i:03}",sn='1',dob='',verbose=0,pres=0);print(z)
			except Exception as e:
				print(e)

	if 0:
		# z=cg(sn='8',rn='14CSR125',dob='31.12.1996');print(z)
		# z=cg(rn='14CSR125',dob='31.12.1996');print(z)
		z=cg(sn=None,rn='15ecr030',dob='28.06.1998');print(z)
		# z=cg(sn='7',rn='15CSR094',dob='28.06.1998');print(z)
		# z=cg(rn='14CSL260',dob='28.06.1998');print(z)
		# z=cg(rn='14CSR125',dob='31.12.1996');print(z)
		# z=cg(sn='4',rn='15CSR094',dob=dobl.get('15CSR094'));print(z)
		# z=cg(rn='14csl260',dob='28.05.1995');print(z)
		# z=cg(rn='17cer162',dob='16.01.2000');print(z)
		
	from pymsgbox import alert
	alert(3)