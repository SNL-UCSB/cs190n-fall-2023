# Imports
from scapy.all import *        # Packet manipulation
import pandas as pd            # Pandas - Create and Manipulate DataFrames
import numpy as np             # Math Stuff (don't worry only used for one line :] )
import binascii                # Binary to Ascii 
import csv

# returns a pandas dataframe containing the fields from the pcap
def pcap_to_df(pcap_name, include_payload=False):

    pcap = rdpcap(pcap_name)
    
    # Collect field names from IP/TCP/UDP (These will be columns in DF)
    ip_fields = [field.name for field in IP().fields_desc]
    tcp_fields = [field.name for field in TCP().fields_desc]
    udp_fields = [field.name for field in UDP().fields_desc]

    dataframe_fields = ip_fields + ['time'] + ["tcp_{}".format(i) for i in tcp_fields] + ["udp_{}".format(i) for i in udp_fields]

    if include_payload:
        dataframe_fields = dataframe_fields + ['payload','payload_raw','payload_hex']

    # Create blank DataFrame
    df = pd.DataFrame(columns=dataframe_fields)
    for packet in pcap[IP]:
        # Field array for each row of DataFrame
        field_values = []
        # Add all IP fields to dataframe
        for field in ip_fields:
            if field == 'options':
                # Retrieving number of options defined in IP Header
                field_values.append(len(packet[IP].fields[field]))
            else:
                field_values.append(packet[IP].fields[field])

        field_values.append(packet.time)

        layer_type = type(packet[IP].payload)
        if packet.haslayer(TCP):
            for field in tcp_fields:
                try:
                    if field == 'options':
                        field_values.append(len(packet[layer_type].fields[field]))
                    else:
                        field_values.append(packet[layer_type].fields[field])
                except:
                    field_values.append(None)
        else:
            for field in tcp_fields:
                field_values.append(None)
                
        if packet.haslayer(UDP):
            for field in udp_fields:
                try:
                    if field == 'options':
                        field_values.append(len(packet[layer_type].fields[field]))
                    else:
                        field_values.append(packet[layer_type].fields[field])
                except:
                    field_values.append(None)
        else:
            for field in udp_fields:
                field_values.append(None)

        if include_payload:
            # Append payload
            field_values.append(len(packet[layer_type].payload))
            field_values.append(packet[layer_type].payload.original)
            field_values.append(binascii.hexlify(packet[layer_type].payload.original))
        
        # Add row to DF
        df_append = pd.DataFrame([field_values], columns=dataframe_fields)
        df = pd.concat([df, df_append], axis=0)

    # Reset Index
    df = df.reset_index()
    # Drop old index column
    df = df.drop(columns="index")
    return df

# returns a CSV containing the fields from the pcap
def pcap_to_csv(pcap, csv_outfile, include_payload=False):
    # Collect field names from IP/TCP/UDP (These will be columns in DF)
    ip_fields = [field.name for field in IP().fields_desc]
    tcp_fields = [field.name for field in TCP().fields_desc]
    udp_fields = [field.name for field in UDP().fields_desc]

    dataframe_fields = ip_fields + ['time'] + ["tcp_{}".format(i) for i in tcp_fields] + ["udp_{}".format(i) for i in udp_fields]

    if include_payload:
        dataframe_fields = dataframe_fields + ['payload','payload_raw','payload_hex']
    
    with open(csv_outfile, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect='unix')

        # write header row
        csv_writer.writerow([''] + dataframe_fields)
        row_number = 0
        for packet in pcap[IP]:
            # Field array for each row of DataFrame
            field_values = []
            # Add all IP fields to dataframe
            for field in ip_fields:
                if field == 'options':
                    # Retrieving number of options defined in IP Header
                    field_values.append(len(packet[IP].fields[field]))
                else:
                    field_values.append(packet[IP].fields[field])

            field_values.append(packet.time)

            layer_type = type(packet[IP].payload)
            if packet.haslayer(TCP):
                for field in tcp_fields:
                    try:
                        if field == 'options':
                            field_values.append(len(packet[layer_type].fields[field]))
                        else:
                            field_values.append(packet[layer_type].fields[field])
                    except:
                        field_values.append(None)
            else:
                field_values = field_values + ([None] * len(tcp_fields))

            if packet.haslayer(UDP):
                for field in udp_fields:
                    try:
                        if field == 'options':
                            field_values.append(len(packet[layer_type].fields[field]))
                        else:
                            field_values.append(packet[layer_type].fields[field])
                    except:
                        field_values.append(None)
            else:
                field_values = field_values + ([None] * len(udp_fields))

            if include_payload:
                # Append payload
                field_values.append(len(packet[layer_type].payload))
                field_values.append(packet[layer_type].payload.original)
                field_values.append(binascii.hexlify(packet[layer_type].payload.original))

            csv_writer.writerow([row_number] + field_values)
            row_number += 1

# returns a CSV containing the fields from the pcap
def split_pcap_to_csv(pcaps_dir, csv_outfile, include_payload=False):
    # Collect field names from IP/TCP/UDP (These will be columns in DF)
    ip_fields = [field.name for field in IP().fields_desc]
    tcp_fields = [field.name for field in TCP().fields_desc]
    udp_fields = [field.name for field in UDP().fields_desc]

    dataframe_fields = ip_fields + ['time'] + ["tcp_{}".format(i) for i in tcp_fields] + ["udp_{}".format(i) for i in udp_fields]

    if include_payload:
        dataframe_fields = dataframe_fields + ['payload','payload_raw','payload_hex']

    filenames = []
    for files in os.listdir(pcaps_dir):
        if files.endswith(".pcap"):
            filenames.append(pcaps_dir + files)

    filenames.sort()
    
    with open(csv_outfile, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect='unix')

        # write header row
        csv_writer.writerow([''] + dataframe_fields)
        row_number = 0

        for files in filenames:
            pcap = rdpcap(files)
            for packet in pcap[IP]:
                # Field array for each row of DataFrame
                field_values = []
                # Add all IP fields to dataframe
                for field in ip_fields:
                    if field == 'options':
                        # Retrieving number of options defined in IP Header
                        field_values.append(len(packet[IP].fields[field]))
                    else:
                        field_values.append(packet[IP].fields[field])

                field_values.append(packet.time)

                layer_type = type(packet[IP].payload)
                if packet.haslayer(TCP):
                    for field in tcp_fields:
                        try:
                            if field == 'options':
                                field_values.append(len(packet[layer_type].fields[field]))
                            else:
                                field_values.append(packet[layer_type].fields[field])
                        except:
                            field_values.append(None)
                else:
                    field_values = field_values + ([None] * len(tcp_fields))

                if packet.haslayer(UDP):
                    for field in udp_fields:
                        try:
                            if field == 'options':
                                field_values.append(len(packet[layer_type].fields[field]))
                            else:
                                field_values.append(packet[layer_type].fields[field])
                        except:
                            field_values.append(None)
                else:
                    field_values = field_values + ([None] * len(udp_fields))

                if include_payload:
                    # Append payload
                    field_values.append(len(packet[layer_type].payload))
                    field_values.append(packet[layer_type].payload.original)
                    field_values.append(binascii.hexlify(packet[layer_type].payload.original))

                csv_writer.writerow([row_number] + field_values)
                row_number += 1
            print("[INFO]: Processed '{}'".format(files))    




'''        
    # Create blank DataFrame
    df = pd.DataFrame(columns=dataframe_fields)
    for packet in pcap[IP]:
        # Field array for each row of DataFrame
        field_values = []
        # Add all IP fields to dataframe
        for field in ip_fields:
            if field == 'options':
                # Retrieving number of options defined in IP Header
                field_values.append(len(packet[IP].fields[field]))
            else:
                field_values.append(packet[IP].fields[field])

        field_values.append(packet.time)

        layer_type = type(packet[IP].payload)
        if packet.haslayer(TCP):
            for field in tcp_fields:
                try:
                    if field == 'options':
                        field_values.append(len(packet[layer_type].fields[field]))
                    else:
                        field_values.append(packet[layer_type].fields[field])
                except:
                    field_values.append(None)
        else:
            for field in tcp_fields:
                field_values.append(None)
                
        if packet.haslayer(UDP):
            for field in udp_fields:
                try:
                    if field == 'options':
                        field_values.append(len(packet[layer_type].fields[field]))
                    else:
                        field_values.append(packet[layer_type].fields[field])
                except:
                    field_values.append(None)
        else:
            for field in udp_fields:
                field_values.append(None)
                
        # Append payload
        field_values.append(len(packet[layer_type].payload))
        field_values.append(packet[layer_type].payload.original)
        field_values.append(binascii.hexlify(packet[layer_type].payload.original))
        
        # Add row to DF
        df_append = pd.DataFrame([field_values], columns=dataframe_fields)
        df = pd.concat([df, df_append], axis=0)

    # Reset Index
    df = df.reset_index()
    # Drop old index column
    df = df.drop(columns="index")
    return df
'''
