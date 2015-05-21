# chef-bits Scripts

## make-chef-ssl-databag.py

Takes an ID and a bunch of PEM-format X.509 certificates and prints out the JSON format required to import into a Chef data bag (which you really want to encrypt).

Written/run using Python 2, have not tested with Python 3.

If it makes you feel better, replace SSL with TLS everywhere in this document and script.

Example:
```
$ ./make-chef-ssl-databag.py --id foo --key mykey.pem --cert mycert.pem > ssl.json
$ knife data bag from file mybag ssl.json --secret-file you_really_should_encrypt_this.pem
```

### Inputs

<table>
  <tr>
    <th>Parameter</th>
    <th>Optional?</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>--id</td>
    <td>No</td>
    <td>ID for this data bag item</td>
  </tr>
  <tr>
    <td>--key</td>
    <td>No</td>
    <td>SSL key in PEM format</td>
  </tr>
  <tr>
    <td>--cert</td>
    <td>No</td>
    <td>SSL certificate in PEM format</td>
  </tr>
  <tr>
    <td>--dhparam</td>
    <td>Yes</td>
    <td>SSL dhparam file in PEM format</td>
  </tr>
  <tr>
    <td>--dhparam</td>
    <td>Yes</td>
    <td>SSL CA file and intermediates in PEM format (for local chain-of-trust, ie OCSP stapling)</td>
  </tr>
</table>

### Outputs

Prints all provided inputs in JSON format suitable for consumption by 'knife data bag from file' to stdout (because $NIX).

### Todo things I thought of but don't need right now

- Error checking (maybe check contents of files?)
- Make field names configurable
- Make script generic for any data bag items (meh)
