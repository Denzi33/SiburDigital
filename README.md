# Sibur Digital

### Description 📝

Here is a code and architecture of test internship task from Sibur Digital.

### Files 📁

- src: the directory of the .py files:
  - common: the directory of executable files:
    - decorators.py: the decorator file of singleton.
    - storage.py: the file for connection to storage.
    - vabus.py: the functionality for working with the data bus.
  - data: the files with data:
    - event.py: the dataclass of event.
    - metric.py: the dataclass of metric.
  - main.py: the starting point of the entire program.
- .gitignore: a gitignore file specifies intentionally untracked files that Git should ignore.
- Dockerfile: a text document that contains all the commands a user could call on the command line to assemble an image.
- pyproject.toml: file acts as a configuration file for packaging-related tools.

### Possible Metrics 📊

- `Count of trips`: (count/mean/median) of completed trips per (week/month/year).
- `Trip difference`: (value/mean/median) of trip arrival difference per (week/month/year) that can be positive or negative.
- `Delays`: (count/percent) of trips per (week/month/year).
- `Usage`: (count/percent) of buses used (week/month/year).
- `Loyalty`: (value/percent) of customer satisfaction with the service.
- `Cost`: (value/mean/median) of the trip.

### Possible Problems ⛔️

- `Incorrect configuration of the data bus`: errors in the configuration of the data bus can lead to failures in the exchange of information between system components. This can manifest itself in the form of data loss or distortion, as well as in a decrease in system performance.
- `Bandwidth limitations`: if the data bus does not have enough bandwidths to process a large amount of data, this can lead to delays in information transmission and reduce overall system performance.
- `Synchronization problems`: when using asynchronous mode of operation with the data bus, it is necessary to ensure correct synchronization between the sender and the recipient of the data. Synchronization errors can lead to data loss or distortion.
- `Network failures`: network problems such as packet loss or data transmission delays can affect the operation of the data bus and cause information exchange failures.
- `Conflicts with other services`: if several services use the same data bus, conflicts in accessing it can cause problems in data exchange.
- `Scalability`: when the load on the system increases, it is necessary to ensure that the data bus is able to process the increased amount of data without reducing performance

### Possible Problems Solutions ✅

- `Configure Data Bus settings`: carefully review the documentation and recommendations for configuring the data bus to ensure its optimal performance and reliability.
- `Ensure sufficient bandwidth`: if a large amount of data is expected, it is necessary to ensure that the data bus is able to handle the load without data loss or distortion.
- `Implement synchronization mechanisms`: use appropriate tools to ensure correct synchronization between the sender and the recipient of the data. This will avoid data loss or duplication.
- `Delimit access to the data bus`: when using the bus by several services, ensure that access to it is delimited to avoid conflicts and problems with data exchange.
- `Scale the system`: as the load on the system increases, consider scaling the data bus to ensure its ability to handle the increased amount of data without compromising performance.

### Possible Service Development ⬆️
- `Expanding functionality`: adding new features and features to users can increase the attractiveness of the service and attract more customers. For example, you can add the ability to integrate with other services or platforms, improve data quality, or expand the geography of coverage.
- `Improving the user experience`: optimizing the interface, increasing the speed of work, improving the quality of service and providing more personalized offers can make the service more convenient and attractive to users.
- `Data Analysis and Analytics`: using data to understand user needs and behaviors can help develop more effective development and marketing strategies. Data analysis can also reveal new opportunities to improve the service.
- `Scaling`: expanding the geography of presence, increasing the number of users or the volume of data processed may require additional resources and investments, but may lead to significant growth and development of the service.
- `Integration with cloud technologies`: using cloud platforms for data storage and processing can simplify scaling and provide more flexible resource management.
