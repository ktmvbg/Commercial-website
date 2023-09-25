import React from "react";
import Avatar from "components/Chat/Avatar/Avatar";


const ChatContent = ({ messages }) => {
  const ref = React.useRef(null);
  React.useEffect(() => {
    if (messages.length) {
      console.log("scrolling");
      ref.current?.scrollIntoView({
        behavior: "smooth",
        block: "end",
      });
    }
  }, [messages.length]);  
  return (
    <div className="max-h-96 h-96 px-6 py-1 overflow-auto">
      {messages.map((message, index) => (
        <div
          key={index}
          className={`py-2 flex flex-row w-full ${
            message.isChatOwner ? "justify-end" : "justify-start"
          }`}
        >
          <div className={`${message.isChatOwner ? "order-2" : "order-1"}`}>
            <Avatar />
          </div>
          <div
            className={`px-2 w-fit py-3 flex flex-col bg-blue-500 rounded-lg text-white ${
              message.isChatOwner ? "order-1 mr-2" : "order-2 ml-2"
            }`}
          >
            <span className="text-xs text-gray-200">
              {message.sentBy}&nbsp;-&nbsp;
              {new Date(message.sentAt).toLocaleTimeString("en-US", {
                hour: "2-digit",
                minute: "2-digit"
              })}
            </span>
            <span className="text-md">{message.text}</span>
          </div>
        </div>
      ))}
      <div ref={ref} />
    </div>
  );
};

export default ChatContent;
