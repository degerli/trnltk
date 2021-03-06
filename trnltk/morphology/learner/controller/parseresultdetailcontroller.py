"""
Copyright  2012  Ali Ok (aliokATapacheDOTorg)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
class ParseResultDetailController(object):
    def __init__(self, sessionmanager):
        """
        @type sessionmanager: SessionManager
        """
        self.sessionmanager = sessionmanager

    def get_calculation_context(self, param_parse_result_uuid):
        calculation_context = self.sessionmanager.get_calculation_context(param_parse_result_uuid)
        if not calculation_context:
            raise Exception("No calculation context found for parse result with UUID : {}".format(param_parse_result_uuid))

        return calculation_context

