U
    jW�_f  �                   @   s�   d dl Z d dlZd dlZd dlmZmZ dZdZdZdZ	dZ
dZd	Zd
Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Ze�  dS )�    N)�post�getz[0mz[31mz[1;32mz[33mz[34mz[35mz[36mz[37mc                   C   s8   t �d� t �d� td� td� td� td� d S )N�clearztoilet -f mono12 -F gay "SMS"� z'[1;32m       -----SPAM SMS SENDER-----z[31m#CODED BY ISURUWA)�os�system�print� r	   r	   �sms.py�banner   s    

r   c                 C   s"   d}| dddd�}t ||d�}d S )Nz'https://guru.lk/auth/headstart/ajax.php�1r   Zsms_reg)ZphoneZcourseZsesskey�action)�data)r   )�number�delayZurlr   Zpossr	   r	   r
   �gurulk   s    r   c                   C   sF   t �  t�d� t�d� t�d� t�d� t�d� t�d� d S )NZcdz
rm -rf SMSz(git clone https://github.com/isuruwa/SMSzcd SMSzpip install -r requirements.txtzpython sms.py)r   r   r   r	   r	   r	   r
   �update   s    




r   c                  C   s\   t �  td� td� td� td� td�} | dkr<t�  | dkrJt�  | dkrXt�  d S )Nr   z[1;32m1.Set Count z[35m2.unlimited z[33mEnter your choice : r   �2)r   r   �input�sms�	unlimited�choice)Zinppr	   r	   r
   r   '   s    r   c                 C   s(   t dt|� d t| � d d � d S )Nz sending ... �	z Sent�
)r   �str)�countr   r	   r	   r
   �sent7   s    r   c                  C   sX   t �  td� td�} td�}td�}d}|t|�k rTt| |� |d7 }t|| � q*d S )Nr   �[35mEnter the number : z[34mEnter the count :z[1;32mEnter the delay time : r   �   )r   r   r   �intr   r   )r   �timesr   r   r	   r	   r
   r   <   s    
r   c                  C   sD   t �  td� td�} td�}d}t| |� |d7 }t|| � q"d S )Nr   r   z[36mEnter the delay time : r   r   )r   r   r   r   r   )r   r   r   r	   r	   r
   r   M   s    
r   c                  C   sb   t �d� t�  td� td� td� td� td� td� td� td�} | dkr^t�  d S )Nr   r   z,[1;32m1.Support for only Sri Lankan Numberszd[34m2.Still contains only one website api. More website apis will be released with future updates.
z6[36mSupport me >> Github - https://github.com/isuruwazJ[34m          >>Facebook - https://www.facebook.com/isuru.umayanga.37819 z![1;32mPress Enter To Continue : )r   r   r   r   r   �ask�Zinpr	   r	   r
   �aboutY   s    
r#   c                  C   s�   t �  td� td� td� td� td� td� td� td�} | dkrTt�  | dkrbt�  | d	krpt�  | d
kr~t�  | dkr�t�  d S )Nr   z[34m1.Start Toolz[35m2.Update Toolz[1;32m3.Aboutz[33m4.Exitz[36mEnter Your Option  >>> r   r   �3�4)r   r   r   r   r   r#   �exitr!   r"   r	   r	   r
   r!   g   s&    r!   )r   �time�sysZrequestsr   r   �W�R�G�O�B�P�CZGRr   r   r   r   r   r   r   r#   r!   r	   r	   r	   r
   �<module>   s*   	