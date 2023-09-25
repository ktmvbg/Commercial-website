import { messages } from "types/Message";

/** This is where we should consume the data
 * from an API
 */
export const useGetMessages = () => {
  return {
    messages: messages
  };
};
