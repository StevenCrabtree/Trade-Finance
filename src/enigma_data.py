'''
Created on Aug 7, 2019

@author: Brian

functions related to the data from the public data site Enigma

Bill of Lading Summary: data fields
    identifier,
    trade_update_date,
    run_date,
    vessel_name,
    port_of_unlading,
    estimated_arrival_date,
    foreign_port_of_lading,
    record_status_indicator,
    place_of_receipt,
    port_of_destination,
    foreign_port_of_destination,
    secondary_notify_party_1,
    actual_arrival_date,
    consignee_name,
    consignee_address,
    consignee_contact_name,
    consignee_comm_number_qualifier,
    consignee_comm_number,
    shipper_party_name,
    shipper_address,
    shipper_contact_name,
    shipper_comm_number_qualifier,
    shipper_comm_number,
    container_number,
    description_sequence_number,
    piece_count,
    description_text,
    harmonized_number,
    harmonized_value,
    harmonized_weight,
    harmonized_weight_unit
'''
import pandas as pd

def read_bill_of_lading_summary(user_data_dir):
    input_file = user_data_dir + "\\" + "BillofLadingSummary-2018.csv"
    df_data = pd.read_csv(input_file, low_memory=False)
    df_data = df_data.set_index('identifier')

    return (df_data)