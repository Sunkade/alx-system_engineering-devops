#!/usr/bin/env puppet
# Using Puppet to create a manifest that kills a process named killmenow.
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}
