# -*- coding: utf-8 -*-

"""
Class object to easily access and manipulte files and folders made under the BIDS convetion

----------------------------------------------------------------------------
 Created by Vincent Ka Ming Cheung on 2018 02 13 
 at the Max Planck Institute for Human Cognitive and Brain Sciences,
 Leipzig, Germany
 
 This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 Internaional License
 
 --- Use at your own risk! While I tried my best, I am not responsible for any errors in the code... ---
 


 
 
EXAMPLE:

from BIDSinterface import BIDS
x = BIDS()
x.homedir = 'path/to/folder'
x.get()
"""


import os

class BIDS: 
    def __init__(self):
        self.homedir = ''      
        self.anat = ''             
        self.func = ''  
        self.doallpath = ''
        self.sub = ''
        self.subpath = ''


    def getsubpath(self):
        "return attribute of list of absolute locations of all subjects"
        sub = []           
        subpath = []
        for folder in os.listdir(self.homedir):
            if 'sub-' in folder:
                subpath.append(os.path.join(self.homedir,folder))  
                sub.append(folder)
        self.subpath = subpath
        self.sub = sub
        
    def getsubsubpath(self, where):
        "return attribute of list of absolute locations of 'where' in all subjects"
        subsubpath = []
        self.getsubpath()
        for sdir in self.subpath:
            for subfolder in os.listdir(sdir):
                if subfolder == where:
                    subsubpath.append(os.path.join(sdir,subfolder))

        if where == 'anat':
            self.anat = subsubpath
        elif where == 'func':
            self.func = subsubpath
        else:
            self.subsubpath = subsubpath
        
    def get(self):
        "get path for anat and func folders for all participants"
        self.getsubsubpath('anat')
        self.getsubsubpath('func')
        self.getsubpath()
        
    def makedirs(self,sublist,subsubfolders):
        """"Make subsubfolders for all participants in sublist
        Example: 
            x = BIDS()
            x.homedir = '/data/pt_neunps166/vincent/rawdicom'
            sublist = [format(id,'02') for id in range(1,21)]
            subsubfolders = ['anat']
            x.makedirs(sublist,subsubfolders)"""
        for sub in sublist:
            for subsub in subsubfolders:
                os.makedirs(os.path.join(self.homedir,'sub-'+sub, subsub))
                print 'Making folder ' + subsub + ' for sub-'+sub


                
    def doall(self, var, kwargs):
        """Apply var with kwargs to all files in self.doallpath
        Example:
            x = BIDS()
            x.homedir = '/data/pt_neunps164/neuroimaging/preprocessing/realign_and_unwarp'
            x.get()
            x.doallpath = x.subpath
            x.doall(gzip,{'keyword','_task-music_run-2_bold_despike.nii'})"""
        
        if len(self.doallpath) == 0:
            raise ValueError('doallpath is empty')
        output = []
        for n, s in enumerate(self.doallpath):
            for files in os.listdir(s):
                self.doall_n = n
                self.doall_s = s
                self.doall_files = files
                out = var(self, **kwargs)  
                output.append(out)               
        output = [o for o in output if o != None]
        return output

# CAN'T PARALLELISE IN A FUNCTION
#    from joblib import Parallel, delayed 
#    def system(command):
#        os.system(command)
#        
#    Parallel(n_jobs=ncores)(delayed(system)(command) for command in command_vec)   


def gzip(B, keyword, match = 'exact'):
    """"Look for keyword and run command
    if match == 'exact' then files must be an exact match with keyword
    if match == 'partial' then command is run as long as keyword matches filename
    Example: 
        x.homedir = '/data/pt_neunps164/neuroimaging/preprocessing/realign_and_unwarp/'
        x.get()
        x.doallpath = x.subpath
        for sub in x.sub:
            for r in str(range(1,6)):
                keyword = 'u' + sub + '_task-music_run-' + r + '_bold_despike.nii'
                # e.g. usub-1103_task-music_run-1_bold_despike.nii
                x.doall(gzip,{'keyword':keyword, 'match': 'exact'})
                
        # BUT THIS IS SLOWER THAN
        for sub in x.sub:
            keyword = 'u' + sub + '_task-music_run-1_bold_despike.nii'
            x.doall(gzip,{'keyword':keyword, 'match': 'exact'})
            keyword = 'u' + sub + '_task-music_run-2_bold_despike.nii'
            x.doall(gzip,{'keyword':keyword, 'match': 'exact'})
            keyword = 'u' + sub + '_task-music_run-3_bold_despike.nii'
            x.doall(gzip,{'keyword':keyword, 'match': 'exact'})
            keyword = 'u' + sub + '_task-music_run-4_bold_despike.nii'
            x.doall(gzip,{'keyword':keyword, 'match': 'exact'})
            keyword = 'u' + sub + '_task-music_run-5_bold_despike.nii'
            x.doall(gzip,{'keyword':keyword, 'match': 'exact'})    
    """
    if match != 'partial':
        if  keyword == B.doall_files:
            filepath = os.path.join(B.doall_s, B.doall_files)
            command = 'gunzip -f ' + filepath             
            return command
    else:
        if keyword in B.doall_files:
            filepath = os.path.join(B.doall_s, B.doall_files)
            command = 'gunzip -f ' + filepath                  
            return command

def checkfile(B, keyword):
    "Look for keyword in self.doallpath"
    if keyword in B.doall_files:
        print 'Found ' + B.doall_files + ' in ' + B.doall_s
        return os.path.join(B.doall_s,B.doall_files)
        
                
def remove(B, keyword):
    "Delete exact matches of file in B.doallpath"
    if  keyword == B.doall_files:
        print 'Remove function temporarily disabled. Uncomment code to reenable.'
#        os.remove(os.path.join(B.doall_s, B.doall_files)  )
   
def despike(B, keyword, preprocdir, run='command'):
    if keyword in B.doall_files:
        command = 'AFNI 3dDespike -NEW -prefix ' + \
                    os.path.join(preprocdir, B.sub[B.doall_n], 'despiked_'+B.doall_files) + \
                    ' ' + \
                    os.path.join(B.doall_s, B.doall_files)
        if run == 'run':
            os.system(command)
        return command


    
#class Methods(BIDS):
#    def __init__(self):
#       BIDS.__init__(self)
#      
