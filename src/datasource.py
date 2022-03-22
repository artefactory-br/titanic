"""Datasource Utils Module for Google Cloud Platform Storage
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

from google.cloud import storage
import pandas as pd


def list_blobs_with_prefix(bucket_name, prefix, delimiter=None):
    """List all the file names in a bucket folder.
    Parameters:
    bucket_name -- name of the Google Storage bucket
    prefix      -- hierarchy of folders and subfolders names ex.: 'root_folder/first_child/second_child/'
    delimiter   -- (optional) delimiter character used with prefix to emulate hierarchy
    Output:
    Returns a list with all the files within a folder
    """
    storage_client = storage.Client()

    blobs = storage_client.list_blobs(bucket_name, prefix=prefix, delimiter=delimiter)

    names = []
    for blob in blobs:
        names.append(blob.name)

    return names


def read_dataframe_from_bucket_file(bucket_name, filename, sep=";"):
    """Read a file in a bucket folder and return a dataframe.

    Parameters:
    bucket_name   -- name of the Google Storage bucket
    filename      -- path to file ex.: 'root_folder/first_child/second_child/filename.ext'

    Output:
    Returns a dataframe with the data from the bucket file
    """
    df = pd.read_csv("gs://" + bucket_name + "/" + filename, sep=sep)

    return df
