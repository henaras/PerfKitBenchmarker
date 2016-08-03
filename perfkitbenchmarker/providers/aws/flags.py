# Copyright 2015 PerfKitBenchmarker Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from perfkitbenchmarker import flags

flags.DEFINE_string('aws_user_name', 'ubuntu',
                    'This determines the user name that Perfkit will '
                    'attempt to use. This must be changed in order to '
                    'use any image other than ubuntu.')
flags.DEFINE_integer('aws_provisioned_iops', None,
                     'IOPS for Provisioned IOPS (SSD) volumes in AWS.')

flags.DEFINE_string('aws_emr_loguri', None,
                    'The log-uri parameter to pass to AWS when creating a '
                    'cluster.  If not set, a bucket will be created.')

flags.DEFINE_string('aws_multiple_enis', False,
                    'Creates multiple Elastic Network Interfaces per instance,'
                    ' which will increase packet per second limit, but '
                    'benchmarks need to be aware of multiple internal ips in '
                    'order to benefit from it.')
