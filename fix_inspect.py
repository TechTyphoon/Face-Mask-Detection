"""
Fix for Python 3.12 compatibility with older Keras versions
"""
import inspect

# Add ArgSpec back to inspect module for compatibility
if not hasattr(inspect, 'ArgSpec'):
    inspect.ArgSpec = inspect.FullArgSpec
