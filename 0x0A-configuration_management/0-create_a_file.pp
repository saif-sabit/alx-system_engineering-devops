# Create new file
file{'/tmp/school':
  ensure => file,
  owner => 'www-data',
  group => 'www-data',
  privildge => '0744',
  content => 'I love Puppet'
}