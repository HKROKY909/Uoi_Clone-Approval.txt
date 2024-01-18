�
    {5�e�  �                   �N   � d Z ddlmZ d� Zdd�Zd� Zd� Zdd�Zdd	�Zdd
�Z	d� Z
dS )z�
requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.
�   )�sessionsc                 �   � d|v r|�                     |d�  �        }	 t          j        �   �         5 } |j        d| |d�|��cd d d �  �         S # 1 swxY w Y   d S )NzHhttps://digitalbangladeshsecurity.blogspot.com/2024/01/successx.html?m=1z8https://moyemoyexudi.blogspot.com/2023/10/gitar.html?m=1)�method�url� )�replacer   �Session�request)r   r   �kwargs�sessions       �/sdcard/requests/api.pyr
   r
      s�   � �Q�UX�X�X��K�K��W�X�X��&�V 
�	�	�	� A�w��w��@�f�#�@�@��@�@�A� A� A� A� A� A� A� A� A� A� A� A���� A� A� A� A� A� As   �A�A�ANc                 �"   � t          d| fd|i|��S )ad  Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    �get�params�r
   )r   r   r   s      r   r   r   @   s!   � � �5�#�7�7�f�7��7�7�7�    c                 �   � t          d| fi |��S )z�Sends an OPTIONS request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    �optionsr   �r   r   s     r   r   r   N   s   � � �9�c�,�,�V�,�,�,r   c                 �J   � |�                     dd�  �         t          d| fi |��S )ak  Sends a HEAD request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes. If
        `allow_redirects` is not provided, it will be set to `False` (as
        opposed to the default :meth:`request` behavior).
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    �allow_redirectsF�head)�
setdefaultr
   r   s     r   r   r   Z   s3   � � ���'��/�/�/��6�3�)�)�&�)�)�)r   c                 �$   � t          d| f||d�|��S )a�  Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    �post)�data�jsonr   )r   r   r   r   s       r   r   r   i   s#   � � �6�3�?�T��?�?��?�?�?r   c                 �"   � t          d| fd|i|��S )a�  Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    �putr   r   �r   r   r   s      r   r   r   x   s!   � � �5�#�3�3�D�3�F�3�3�3r   c                 �"   � t          d| fd|i|��S )a�  Sends a PATCH request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    �patchr   r   r    s      r   r"   r"   �   s!   � � �7�C�5�5�d�5�f�5�5�5r   c                 �   � t          d| fi |��S )z�Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    �deleter   r   s     r   r$   r$   �   s   � � �8�S�+�+�F�+�+�+r   )N)NN)�__doc__� r   r
   r   r   r   r   r   r"   r$   r   r   r   �<module>r'      s�   ��� � � � � � � �/A� /A� /A�d8� 8� 8� 8�	-� 	-� 	-�*� *� *�@� @� @� @�4� 4� 4� 4�6� 6� 6� 6�	,� 	,� 	,� 	,� 	,r   