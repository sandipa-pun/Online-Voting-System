import pandas as pd
from pathlib import Path

path = Path("database")
def count_reset():
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','stdid','name','batch','faculty','password','con password','hasVoted']]
    for index, row in df.iterrows():
        df['hasVoted'].iloc[index]=0
    df.to_csv(path/'voterList.csv')

    df=pd.read_csv(path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    for index, row in df.iterrows():
        df['Vote Count'].iloc[index]=0
    df.to_csv (path/'cand_list.csv')

def reset_voter_list():
    df = pd.DataFrame(columns=['voter_id','stdid','name','batch','faculty','password','con password','hasVoted'])
    df=df[['voter_id','stdid','name','batch','faculty','password','con password','hasVoted']]
    df.to_csv(path/'voterList.csv')

def reset_cand_list():
    df = pd.DataFrame(columns=['Sign','Name','Vote Count'])
    df=df[['Sign','Name','Vote Count']]
    df.to_csv(path/'cand_list.csv')


def verify(vid,password):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','password','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==vid and df['password'].iloc[index]==password:
            return True
    return False


def isEligible(vid):
    df=pd.read_csv(path/'voterList.csv')
    df=df[['voter_id','stdid','name','batch','faculty','password','con password','hasVoted']]
    for index, row in df.iterrows():
        if df['voter_id'].iloc[index]==vid and df['hasVoted'].iloc[index]==0:
            return True
    return False


def vote_update(st,vid):
    if isEligible(vid):
        df=pd.read_csv (path/'cand_list.csv')
        df=df[['Sign','Name','Vote Count']]
        for index, row in df.iterrows():
            if df['Sign'].iloc[index]==st:
                df['Vote Count'].iloc[index]+=1

        df.to_csv (path/'cand_list.csv')

        df=pd.read_csv(path/'voterList.csv')
        df=df[['voter_id','stdid','name','batch','faculty','password','con password','hasVoted']]
        for index, row in df.iterrows():
            if df['voter_id'].iloc[index]==vid:
                df['hasVoted'].iloc[index]=1

        df.to_csv(path/'voterList.csv')

        return True
    return False


def show_result():
    df=pd.read_csv (path/'cand_list.csv')
    df=df[['Sign','Name','Vote Count']]
    v_cnt = {}
    for index, row in df.iterrows():
        v_cnt[df['Sign'].iloc[index]] = df['Vote Count'].iloc[index]

    return v_cnt


def xor_cipher(text, key):
    ciphered_text = ""
    for i in range(len(text)):
        ciphered_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return ciphered_text

def encrypt(password, key="secret_key"):
    return xor_cipher(password, key)

def decrypt(encrypted_password, key="secret_key"):
    return xor_cipher(encrypted_password, key)


def taking_data_voter(stdid, name, batch, faculty, password, conpass):
    encrypted_password = encrypt(password)
    encrypted_conpass = encrypt(conpass)

    df = pd.read_csv(path / 'voterList.csv')
    df = df[['voter_id', 'stdid', 'name', 'batch', 'faculty', 'password', 'con password', 'hasVoted']]
    
    row, col = df.shape
    if row == 0:
        vid = 10001
        df = pd.DataFrame({"voter_id": [vid],
                           "stdid": [stdid],
                           "name": [name],
                           "batch": [batch],
                           "faculty": [faculty],
                           "password": [encrypted_password],
                           "con password": [encrypted_conpass],
                           "hasVoted": [0]}, )
    else:
        vid = df['voter_id'].iloc[-1] + 1
        df1 = pd.DataFrame({"voter_id": [vid],
                            "stdid": [stdid],
                            "name": [name],
                            "batch": [batch],
                            "faculty": [faculty],
                            "password": [encrypted_password],
                            "con password": [encrypted_conpass],
                            "hasVoted": [0]}, )

        df = pd.concat([df, df1], ignore_index=True)

    df.to_csv(path / 'voterList.csv')

    return vid

def voterdetails():
    df = pd.read_csv(path / 'voterList.csv')
    df = df[['voter_id', 'stdid', 'name', 'batch', 'faculty', 'password', 'hasVoted']]

    voter_details = []
    for index, row in df.iterrows():
        decrypted_password = decrypt(row['password'])
        voter_details.append({
            'Voter ID': row['voter_id'],
            'Student ID': row['stdid'],
            'Name': row['name'],
            'Batch': row['batch'],
            'Faculty': row['faculty'],
            'password': decrypted_password,
            'Has Voted': row['hasVoted']
        })

    return voter_details



