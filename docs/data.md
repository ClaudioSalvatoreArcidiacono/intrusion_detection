## Data Sources

### Getting the data

Data will not be published to git. In order to download the data run in in a terminal shell from the project folder the following commands:

```bash
# Download data, 10 percent only
wget -N http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz
# Download headers
wget -N http://kdd.ics.uci.edu/databases/kddcup99/kddcup.names
# Move data to folder
mv kddcup* data
# Unzip
echo n | gunzip data/kddcup.data_10_percent.gz
```

### Dataset Description

"*This is the data set used for The Third International Knowledge Discovery and Data Mining Tools Competition, which was held in conjunction with KDD-99 The Fifth International Conference on Knowledge Discovery and Data Mining. The competition task was to build a network intrusion detector, a predictive model capable of distinguishing between `bad` connections, called intrusions or attacks, and `good` normal connections. This database contains a standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment.*"

source: [KDD Cup 1999 Data](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

#### Features Description

<TABLE BORDER WIDTH="80%" NOSAVE >
<TR NOSAVE>
<TD><I>feature name</I></TD>

<TD NOSAVE><I>description&nbsp;</I></TD>

<TD><I>type</I></TD>
</TR>

<TR>
<TD>duration&nbsp;</TD>

<TD>length (number of seconds) of the connection&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>protocol_type&nbsp;</TD>

<TD>type of the protocol, e.g. tcp, udp, etc.&nbsp;</TD>

<TD>discrete</TD>
</TR>

<TR>
<TD>service&nbsp;</TD>

<TD>network service on the destination, e.g., http, telnet, etc.&nbsp;</TD>

<TD>discrete</TD>
</TR>

<TR>
<TD>src_bytes&nbsp;</TD>

<TD>number of data bytes from source to destination&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>dst_bytes&nbsp;</TD>

<TD>number of data bytes from destination to source&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>flag&nbsp;</TD>

<TD>normal or error status of the connection&nbsp;</TD>

<TD>discrete&nbsp;</TD>
</TR>

<TR>
<TD>land&nbsp;</TD>

<TD>1 if connection is from/to the same host/port; 0 otherwise&nbsp;</TD>

<TD>discrete</TD>
</TR>

<TR>
<TD>wrong_fragment&nbsp;</TD>

<TD>number of ``wrong'' fragments&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>urgent&nbsp;</TD>

<TD>number of urgent packets&nbsp;</TD>

<TD>continuous</TD>
</TR>

<CAPTION ALIGN=BOTTOM>&nbsp;
<BR>Table 1: Basic features of individual TCP connections.</CAPTION>
</TABLE>
&nbsp;
<TABLE BORDER WIDTH="80%" NOSAVE >
<TR>
<TD><I>feature name</I></TD>

<TD><I>description&nbsp;</I></TD>

<TD><I>type</I></TD>
</TR>

<TR>
<TD>hot&nbsp;</TD>

<TD>number of ``hot'' indicators</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>num_failed_logins&nbsp;</TD>

<TD>number of failed login attempts&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>logged_in&nbsp;</TD>

<TD>1 if successfully logged in; 0 otherwise&nbsp;</TD>

<TD>discrete</TD>
</TR>

<TR>
<TD>num_compromised&nbsp;</TD>

<TD>number of ``compromised'' conditions&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>root_shell&nbsp;</TD>

<TD>1 if root shell is obtained; 0 otherwise&nbsp;</TD>

<TD>discrete</TD>
</TR>

<TR>
<TD>su_attempted&nbsp;</TD>

<TD>1 if ``su root'' command attempted; 0 otherwise&nbsp;</TD>

<TD>discrete</TD>
</TR>

<TR>
<TD>num_root&nbsp;</TD>

<TD>number of ``root'' accesses&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>num_file_creations&nbsp;</TD>

<TD>number of file creation operations&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>num_shells&nbsp;</TD>

<TD>number of shell prompts&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>num_access_files&nbsp;</TD>

<TD>number of operations on access control files&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR NOSAVE>
<TD>num_outbound_cmds</TD>

<TD NOSAVE>number of outbound commands in an ftp session&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>is_hot_login&nbsp;</TD>

<TD>1 if the login belongs to the ``hot'' list; 0 otherwise&nbsp;</TD>

<TD>discrete</TD>
</TR>

<TR>
<TD>is_guest_login&nbsp;</TD>

<TD>1 if the login is a ``guest''login; 0 otherwise&nbsp;</TD>

<TD>discrete</TD>
</TR>

<CAPTION ALIGN=BOTTOM>&nbsp;
<BR>Table 2: Content features within a connection suggested by domain knowledge.</CAPTION>
</TABLE>
&nbsp;
<TABLE BORDER WIDTH="80%" NOSAVE >
<TR>
<TD><I>feature name</I></TD>

<TD><I>description&nbsp;</I></TD>

<TD><I>type</I></TD>
</TR>

<TR>
<TD>count&nbsp;</TD>

<TD>number of connections to the same host as the current connection in
the past two seconds&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD></TD>

<TD><I>Note: The following&nbsp; features refer to these same-host connections.</I></TD>

<TD></TD>
</TR>

<TR>
<TD>serror_rate&nbsp;</TD>

<TD>% of connections that have ``SYN'' errors&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>rerror_rate&nbsp;</TD>

<TD>% of connections that have ``REJ'' errors&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>same_srv_rate&nbsp;</TD>

<TD>% of connections to the same service&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>diff_srv_rate&nbsp;</TD>

<TD>% of connections to different services&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>srv_count&nbsp;</TD>

<TD>number of connections to the same service as the current connection
in the past two seconds&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD></TD>

<TD><I>Note: The following features refer to these same-service connections.</I></TD>

<TD></TD>
</TR>

<TR>
<TD>srv_serror_rate&nbsp;</TD>

<TD>% of connections that have ``SYN'' errors&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>srv_rerror_rate&nbsp;</TD>

<TD>% of connections that have ``REJ'' errors&nbsp;</TD>

<TD>continuous</TD>
</TR>

<TR>
<TD>srv_diff_host_rate&nbsp;</TD>

<TD>% of connections to different hosts&nbsp;</TD>

<TD>continuous&nbsp;</TD>
</TR>

<CAPTION ALIGN=BOTTOM>&nbsp;
<BR>Table 3: Traffic features computed using a two-second time window.</CAPTION>
</TABLE>


source: [KDD Cup 1999 Data-Task description](http://kdd.ics.uci.edu/databases/kddcup99/task.html)
